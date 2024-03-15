from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from core.utils.states_schedule import StepsGetSchedule
import core.utils
from core.utils.utils import get_column_for_class, get_day_of_week_row, get_schedule
from core.keyboards.kb import keyboard_days_of_week, get_num_builder, keyboard_yes_no


async def get_schedule_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, Выбери день недели:', reply_markup=keyboard_days_of_week)
    # await message.answer(f'{message.from_user.first_name}, ты выбрал {message.text}',
    #                      reply_markup=ReplyKeyboardRemove())
    await state.set_state(StepsGetSchedule.GET_DAY)
    await message.delete()


async def get_day(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, Введи цифру и букву класса:')
                         # reply_markup=ReplyKeyboardRemove())
    await state.update_data(day=message.text)
    await state.set_state(StepsGetSchedule.GET_NUM_AND_LETTER)
    await message.delete()


async def get_num_and_letter(message: Message, state: FSMContext):
    context_data = await state.get_data()
    await message.answer(f'Ты выбрал день недели:\r\n{context_data.get("day")}\r\nТы выбрал букву и номер класса: \r\n{message.text}\r\n',
                         reply_markup=keyboard_yes_no)
    await state.update_data(num_and_letter=message.text)
    await state.set_state(StepsGetSchedule.GET_SCHEDULE)
    # Здесь необходимо дать возможность пользователю вернуться в начало анкеты


async def get_schedule_from_sparky(message: Message, state: FSMContext):

    context_data = await state.get_data()
    await message.answer(f'Сохраненные данные в машине состояний:\r\n{str(context_data)}')

    day_of_week = str(context_data.get('day'))
    num_and_letter = str(context_data.get('num_and_letter'))
    print(day_of_week, num_and_letter)

    # print(get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row(day_of_week)))
    #Получаем расписание
    list_of_lessons = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row(day_of_week))

    #Пояснение как работает мап и джоин
    # lessons_string = ''
    # for lesson in list_of_lessons:
    #     lessons_string += str(lesson)
    #     lessons_string += '\n '
    # print(lessons_string)

    lessons_string = '\n'.join(map(str, list_of_lessons)) #Здесь мы используем метод джоин и мап для форматирования списка в удобную для отправки строку
    print(lessons_string)

    data_user = f'Вот твое расписание \r\n' \
                f'Выбранный день недели: {day_of_week}\r\n' \
                f'Выбранный класс: {num_and_letter}\r\n' \

    await message.answer(data_user)
    await message.answer(lessons_string)

    await state.clear()