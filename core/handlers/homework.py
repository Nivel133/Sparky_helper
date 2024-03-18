from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from core.utils.states_homework import StepsCreateHomework
from core.keyboards.kb_hw import ikb_confirm, keyboard_main_hw
from core.keyboards.kb import keyboard_main_menu

from core.data import sql_hw



async def main_hw(message: Message):
    await message.answer(f'Что ты хочешь сделать со своим домашним заданием?', reply_markup=keyboard_main_hw)

async def find_all_hw(message: Message):
    all_hw_from_user = await sql_hw.get_all_hw(message.from_user.id)
    await message.answer(f'Вот все домашние задания, которые ты записал: \n\n\n'
                         f'{all_hw_from_user}', reply_markup=keyboard_main_menu)

async def start_write_hw(message: Message, state: FSMContext):
    await message.answer(f'Введи дз, которое хочешь сохранить сюда\n'
                         f'!!!Не забудь уточнить на какой предмет и на какой день ты записываешь!!!\n'
                         f'Пример: матеша, вторник уч 56 стр 77,78,79,83 упр доделать!')
    await state.set_state(StepsCreateHomework.WRITE_HW)

async def execute_hw(message: Message, state: FSMContext):
    await message.answer('Мы сейчас запустили EXECUTE')
    userid = str(message.from_user.id)
    # texthw = str(message.text)
    await state.update_data(text_hw=message.text)
    await state.update_data(user_id=userid)
    context_data = await state.get_data()
    print(context_data)
    # await sql_hw.create_hw(userid, texthw)
    await message.answer(f'Твой id: {message.from_user.id} \n'
                         f'Ты хочешь записать дз: {context_data.get(message.text)}\n'
                         f'Данные в хранилище: {context_data}'
                         f'Всё верно?', reply_markup=ikb_confirm)


async def yes_hw(call: CallbackQuery, state: FSMContext, bot: Bot):
    context_data = await state.get_data()
    userid = context_data.get('user_id')
    texthw = context_data.get('text_hw')
    await sql_hw.create_hw(userid, texthw)
    await state.clear()
    await bot.send_message(userid, f'Данные успешно сохранены', reply_markup=keyboard_main_hw)
    await call.answer()


async def no_hw(call: CallbackQuery, state: FSMContext, bot: Bot):
    context_data = await state.get_data()
    userid = context_data.get('user_id')
    await bot.send_message(userid, f'Напишите домашнее заданее заного')
    await state.set_state(StepsCreateHomework.WRITE_HW)
    await call.answer()
