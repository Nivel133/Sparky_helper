from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from core.utils.states_schedule import StepsGetSchedule
from core.utils.utils import get_column_for_class, get_day_of_week_row, get_schedule
from core.keyboards.kb import keyboard_days_of_week, ikb_confirm_schedule, keyboard_main_menu, keyboard_yes_no
import emoji


async def start(message: Message):
    await message.answer(f'Спасибо, что воспользовались моим ботом, {message.from_user.first_name} !\n'
    f'Отправь мне команду start повторно, если захочешь вернуться в главное меню\n', reply_markup=keyboard_main_menu)


async def get_schedule_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, Выбери день недели: ' + emoji.emojize(":brain:"),
                         reply_markup=keyboard_days_of_week)
    await state.set_state(StepsGetSchedule.GET_DAY)


async def get_day(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, Введи цифру и букву класса слитно, без пробелов и кавычек\n'
                         f'Пример: 7б, 5в, 11а')
                         # reply_markup=ReplyKeyboardRemove())
    await state.update_data(day=message.text)
    await state.update_data(user_id=message.from_user.id)
    await state.set_state(StepsGetSchedule.GET_NUM_AND_LETTER)



async def get_num_and_letter(message: Message, state: FSMContext):
    context_data = await state.get_data()
    await state.update_data(num_and_letter=message.text)
    await message.answer(f'Ты выбрал день недели:\r\n{context_data.get("day")}\r\n'
                         f'Ты выбрал букву и номер класса: \r\n{message.text}\r\n',
                         reply_markup=keyboard_yes_no)
    await state.set_state(StepsGetSchedule.GET_SCHEDULE)
    # Здесь необходимо дать возможность пользователю вернуться в начало анкеты

# async def get_yes(message: Message, state: FSMContext):
#     context_data = await state.get_data()
#     await message.answer(f'Ищу твоё расписание')
#     await state.set_state(StepsGetSchedule.GET_SCHEDULE)
#
# async def get_no(message: Message, state: FSMContext):
#     context_data = await state.get_data()
#     await message.answer(f'Давай попробуем снова!\n'
#                          f'Выбери день недели!', reply_markup=keyboard_days_of_week)
#     await state.set_state(StepsGetSchedule.GET_DAY)

# async def get_yes(call: CallbackQuery, state: FSMContext, bot: Bot):
#     print(call)
#     await state.set_state(StepsGetSchedule.GET_SCHEDULE)
#     # await call.answer()
#
#
async def get_no(message: Message, state: FSMContext):
    print('я отработала')
    # context_data = await state.get_data()
    # print(context_data)
    await message.answer(f'что-то', reply_markup=keyboard_days_of_week)
    await state.clear()
    await state.set_state(StepsGetSchedule.GET_DAY)

async def get_schedule_from_sparky(message: Message, state: FSMContext):
    context_data = await state.get_data()
    print(context_data)
    # await message.answer(f'Сохраненные данные в машине состояний:\r\n{str(context_data)}')
    day_of_week = str(context_data.get('day'))
    num_and_letter = str(context_data.get('num_and_letter'))
    #Получаем расписание
    list_of_lessons, list_of_rooms = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row(day_of_week))

    #Пояснение как работает мап и джоин
    lessons_string = ''
    for lesson, room in zip(list_of_lessons, list_of_rooms):
        lessons_string += str(lesson)
        lessons_string += ' КАБ '
        lessons_string += str(room)
        lessons_string += '\n '
    print(lessons_string)

    # lessons_string = '\n'.join(map(str, list_of_lessons)) #Здесь мы используем метод джоин и мап для форматирования списка в удобную для отправки строку

    data_user = f'Вот твое расписание \r\n' \
                f'Выбранный день недели: {day_of_week}\r\n' \
                f'Выбранный класс: {num_and_letter}\r\n' \

    await message.answer(data_user, reply_markup=keyboard_main_menu)
    # await message.answer(lessons_string)

    await state.clear()



async def get_no(message: Message, state: FSMContext):
    await state.clear()

