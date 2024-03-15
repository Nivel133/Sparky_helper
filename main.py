from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message
import logging
from aiogram.filters import Command
from core.settings import settings
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from core.handlers.get_schedule_handlers import get_schedule_form, get_day, get_num_and_letter, get_schedule_from_sparky
from core.utils.states_schedule import StepsGetSchedule
from core.handlers.reply import router

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот выключен!")

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

    dp.message.register(get_schedule_form, Command(commands='form'))
    dp.message.register(get_day, StepsGetSchedule.GET_DAY)
    dp.message.register(get_num_and_letter, StepsGetSchedule.GET_NUM_AND_LETTER)
    dp.message.register(get_schedule_from_sparky, StepsGetSchedule.GET_SCHEDULE)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
