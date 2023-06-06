from aiogram.dispatcher.filters.state import State, StatesGroup


class UserRegister(StatesGroup):
    input_name = State()