import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from database.db import Database
from loader import bot_method

db = Database('database/db.db')



async def search_start_message_handler(message: types.Message, state: FSMContext):
    if not db.check_available_search_user(message.from_user.id):
        list_users = db.get_all_users_search()
        if len(list_users) == 0:
            await message.answer("В данный момент в поиске нет людей, ты был добавлен в ожидание.")
            db.add_search_await(message.from_user.id)
        else:
            random_people_id = random.randint(0, len(list_users) - 1)
            random_user_id = list_users[random_people_id][0] if list_users[random_people_id][0] is not None else \
            list_users[random_people_id][1]
            await bot_method.send_message(chat_id=random_user_id, text="Собеседник покдлючился к чату")
            db.add_companion_user(random_user_id, message.from_user.id)
            await message.answer("Мы нашли тебе собеседника!")
    else:
        await message.answer("Извини, но ты уже находишься в поиске или уже нашёл себе собеседника!")


async def search_start_callback_handler(call: types.CallbackQuery, state: FSMContext):
    if not db.check_available_search_user(call.from_user.id):
        list_users = db.get_all_users_search()
        if len(list_users) == 0:
            await call.message.edit_text("В данный момент в поиске нет людей, ты был добавлен в ожидание.")
            db.add_search_await(call.from_user.id)
        else:
            random_people_id = random.randint(0, len(list_users)-1)
            random_user_id = list_users[random_people_id][0] if list_users[random_people_id][0] is not None else \
                list_users[random_people_id][1]
            await bot_method.send_message(chat_id=random_user_id, text="Собеседник покдлючился к чату")
            db.add_companion_user(random_user_id, call.from_user.id)
            await call.message.edit_text("Мы нашли тебе собеседника!")
    else:
        await call.message.edit_text("Извини, но ты уже находишься в поиске или уже нашёл себе собеседника!")

