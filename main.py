from aiogram import Bot, Dispatcher, F
import asyncio
import emoji
from aiogram.types import Message
import logging
from aiogram.filters import Command
from core.settings import settings
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from core.handlers.get_schedule_handlers import get_schedule_form, get_day, get_num_and_letter,\
    get_schedule_from_sparky, get_no, start
from core.utils.states_schedule import StepsGetSchedule
from core.utils.states_homework import StepsCreateHomework
from core.handlers.reply import router
from core.handlers.homework import execute_hw, start_write_hw, main_hw, yes_hw, no_hw, find_all_hw, back_to_menu_hw
from core.data import sql_hw
from core.handlers import text


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text=text.onstartup_text)
    await sql_hw.db_connect()

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text=text.onendup_text)

# git remote add amvera https://git.amvera.ru/nivel/sparky_helper_bot)
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    # dp.message.register(get_start)

    dp.message.register(start, Command(commands="start"))

    dp.message.register(get_schedule_form, F.text == 'Расписание')
    dp.message.register(get_no, F.text == '❌')
    # dp.message.register(get_yes, F.text == '✅')
    # dp.callback_query.register(get_yes, F.data.startswith('sch_yes'))
    # dp.callback_query.register(get_no, F.data.startswith('sch_no'))
    dp.message.register(get_day, StepsGetSchedule.GET_DAY)
    dp.message.register(get_num_and_letter, StepsGetSchedule.GET_NUM_AND_LETTER)
    dp.message.register(get_schedule_from_sparky, StepsGetSchedule.GET_SCHEDULE)

    dp.message.register(main_hw, F.text == 'Домашнее Задание')
    dp.message.register(start_write_hw, F.text == 'Записать')
    dp.message.register(find_all_hw, F.text == 'Посмотреть')
    dp.message.register(back_to_menu_hw, F.text == '🔙')
    dp.message.register(execute_hw, StepsCreateHomework.WRITE_HW)
    dp.callback_query.register(yes_hw, F.data.startswith('yes_hw'))
    dp.callback_query.register(no_hw, F.data.startswith('no_hw'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())


# ssh-keygen
# type C:\Users\User/.ssh/id_rsa.pub
# ssh root@92.53.10*.231
#
#
# sudo apt update
# sudo apt upgrade
# sudo apt --reinstall install python3 -y
# sudo apt --reinstall install python3-pip -y
#
# sudo apt install nodejs
# sudo apt install npm
# npm install pm2 -g

# pip3 install -r requierements.txt
#  pm2 start main.py --interpreter=python3
# pm2 status
# pm2 monit
# delete main

# git pull
