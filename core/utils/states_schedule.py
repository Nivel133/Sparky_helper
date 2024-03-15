from aiogram.fsm.state import StatesGroup, State


class StepsGetSchedule(StatesGroup):
    GET_DAY = State()
    GET_NUM_AND_LETTER = State()
    GET_SCHEDULE = State()