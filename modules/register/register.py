from aiogram import types
from aiogram.dispatcher import FSMContext

from database.db import Database
from modules.register.states.register_states_class import UserRegister
from utils.generate_messages.generate_register import generator_message_register_message_already, \
    generate_message_register_step_1

db = Database('database/db.db')


async def register_message_handler(message: types.Message, state: FSMContext):
    if not db.check_available_user(message.from_user.id):
        text = await generate_message_register_step_1()
        await message.answer(text=text, parse_mode="MarkdownV2")
        await UserRegister.input_name.set()
    else:
        text, keyboard = await generator_message_register_message_already(message.from_user.first_name)
        await message.answer(text=text, reply_markup=keyboard, parse_mode="MarkdownV2")


async def register_callback_handler(call: types.CallbackQuery, state: FSMContext):
    if call.data == "register":
        if not db.check_available_user(call.from_user.id):
            text = await generate_message_register_step_1()
            await call.message.edit_text(text=text, parse_mode="MarkdownV2")
            await UserRegister.input_name.set()
        else:
            text, keyboard = await generator_message_register_message_already(call.from_user.first_name)
            await call.message.edit_text(text=text, reply_markup=keyboard, parse_mode="MarkdownV2")
