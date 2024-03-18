from aiogram.fsm.state import StatesGroup, State


class StepsCreateHomework(StatesGroup):
    WRITE_HW = State()
    CONFIRM_AND_SAVE = State()
