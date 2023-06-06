from aiogram import Dispatcher

from utils.decorators.reg_decorator import auth_user_message, auth_user_callback
from . import search


async def register_search_handlers(dp: Dispatcher):
    dp.register_message_handler(auth_user_message(search.search_start_message_handler), commands=['search'])
    dp.register_callback_query_handler(auth_user_callback(search.search_start_callback_handler),
                                       lambda c: c.data == "search")
