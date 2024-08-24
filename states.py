from aiogram.dispatcher.filters.state import State, StatesGroup


class OpenBudjetStates(StatesGroup):
    contact = State()
    sms_code = State()