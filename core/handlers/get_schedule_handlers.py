from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.states_schedule import StepsGetSchedule
from core.utils.utils import get_column_for_class, get_day_of_week_row, get_schedule
from core.keyboards.kb import keyboard_days_of_week, keyboard_main_menu, keyboard_yes_no
import emoji
from core.handlers import text


async def start(message: Message):
    await message.answer(text.get_start_text(message.from_user.first_name), reply_markup=keyboard_main_menu)


async def get_schedule_form(message: Message, state: FSMContext):
    await message.answer(f'<b>{message.from_user.first_name},</b> Выбери день недели📆: ',
                         reply_markup=keyboard_days_of_week)
    await state.set_state(StepsGetSchedule.GET_DAY)


async def get_day(message: Message, state: FSMContext):
    await message.answer(text.get_day_text(message.from_user.first_name))
    await state.update_data(day=message.text)
    await state.update_data(user_id=message.from_user.id)
    await state.set_state(StepsGetSchedule.GET_NUM_AND_LETTER)


async def get_num_and_letter(message: Message, state: FSMContext):
    context_data = await state.get_data()
    await state.update_data(num_and_letter=message.text)
    await message.answer(f'📆Ты выбрал день недели:\r\n{context_data.get("day")}\r\n'
                         f'📝Ты выбрал букву и номер класса: \r\n{message.text}\r\n',
                         reply_markup=keyboard_yes_no)

    await state.set_state(StepsGetSchedule.GET_SCHEDULE)


async def get_no(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выбери день снова', reply_markup=keyboard_days_of_week)
    await state.set_state(StepsGetSchedule.GET_DAY)


async def get_schedule_from_sparky(message: Message, state: FSMContext):
    context_data = await state.get_data()
    day_of_week = str(context_data.get('day'))
    num_and_letter = str(context_data.get('num_and_letter'))
    #Получаем расписание
    list_of_lessons, list_of_rooms = get_schedule(get_column_for_class(num_and_letter), get_day_of_week_row(day_of_week))

    #Пояснение как работает мап и джоин
    lessons_string = text.parser_of_lessons_text(list_of_lessons, list_of_rooms) #верстка сообщения с расписанием

    data_user = text.data_user_schedule(day_of_week, num_and_letter) #Отображение в консоль

    await message.answer(data_user+lessons_string, reply_markup=keyboard_main_menu)
    # await message.answer()

    await state.clear()


