from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from core.utils.states_homework import StepsCreateHomework
from core.keyboards.kb_hw import ikb_confirm, keyboard_main_hw
from core.keyboards.kb import keyboard_main_menu
from core.handlers import text
from core.data import sql_hw



async def main_hw(message: Message):
    await message.answer(f'Что ты хочешь сделать со своим домашним заданием❓\n 🤢Кроме того, чтобы забыть о нем😏)', reply_markup=keyboard_main_hw)

async def find_all_hw(message: Message):
    all_hw_from_user = await sql_hw.get_all_hw(message.from_user.id)
    await message.answer(f'Вот все домашние задания, которые ты записал📦: \n\n'
                         f'{all_hw_from_user}', reply_markup=keyboard_main_menu)
    # await message.answer(f'\nЭто домашнее заданее, которое ты записал последним🆕: \n'
    #                      f'🆕{new_message[0]}🆕', reply_markup=keyboard_main_menu)

async def start_write_hw(message: Message, state: FSMContext):
    await message.answer(text=text.enter_hw_text)
    await state.set_state(StepsCreateHomework.WRITE_HW)

async def execute_hw(message: Message, state: FSMContext):
    userid = str(message.from_user.id)
    await state.update_data(text_hw=message.text)
    await state.update_data(user_id=userid)
    # context_data = await state.get_data()
    await message.answer(text=text.execute_hw_text(message.text), reply_markup=ikb_confirm)


async def yes_hw(call: CallbackQuery, state: FSMContext, bot: Bot):
    context_data = await state.get_data()
    userid = context_data.get('user_id')
    texthw = context_data.get('text_hw')
    await sql_hw.create_hw(userid, texthw)
    await state.clear()
    await bot.send_message(userid, f'📥<b>Данные успешно сохранены</b>📥', reply_markup=keyboard_main_hw)
    await call.answer()


async def no_hw(call: CallbackQuery, state: FSMContext, bot: Bot):
    context_data = await state.get_data()
    userid = context_data.get('user_id')
    await bot.send_message(userid, f'📝<b>Напишите домашнее заданее заново</b>📝')
    await state.set_state(StepsCreateHomework.WRITE_HW)
    await call.answer()


async def back_to_menu_hw(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f'Возвращаемся в главное меню🔍', reply_markup=keyboard_main_menu)
