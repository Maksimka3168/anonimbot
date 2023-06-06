from aiogram import Dispatcher

from . import register
from . import states
from .states.register_states_class import UserRegister


async def register_reg_user_handlers(dp: Dispatcher):
    dp.register_message_handler(register.register_message_handler, commands=['register'])
    dp.register_callback_query_handler(register.register_callback_handler,
                                       lambda c: c.data == "register")
    dp.register_message_handler(states.register_states.input_name_message_handler,
                                state=UserRegister.input_name)