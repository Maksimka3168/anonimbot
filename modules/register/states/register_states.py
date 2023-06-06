from aiogram import types
from aiogram.dispatcher import FSMContext

from database.db import Database
from utils.generate_messages.generate_register import generate_message_register_success

db = Database('database/db.db')


async def input_name_message_handler(message: types.Message, state: FSMContext):
    db.register_user(message.from_user.id, message.from_user.username, message.text)
    text, keyboard = await generate_message_register_success()
    await message.answer(text=text, reply_markup=keyboard, parse_mode="MarkdownV2")
    await state.finish()
