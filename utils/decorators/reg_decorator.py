from aiogram import types

from database.db import Database

db = Database('database/db.db')


def auth_user_message(func):
    async def wrapper(message, state):
        if not db.check_available_user(message['from']['id']):
            return await message.answer("☹️Прости, но для того, чтобы использовать данную функцию, тебе "
                                        "нужно пройти *регистрацию*👇\n", parse_mode="MarkdownV2",
                                        reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[
                                            [
                                                types.InlineKeyboardButton(text="😉 Зарегестрироваться",
                                                                           callback_data="register")
                                            ]
                                        ]))
        return await func(message, state)

    return wrapper


def auth_user_callback(func):
    async def wrapper(call, state):
        if not db.check_available_user(call['from']['id']):
            return await call.message.answer("Прости, но для того, чтобы использовать данную функцию, тебе "
                                             "нужно пройти *регистрацию* ☹️\n", parse_mode="MarkdownV2",
                                             reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[
                                                 [
                                                     types.InlineKeyboardButton(text="😉 Зарегестрироваться",
                                                                                callback_data="register")
                                                 ]
                                             ]))
        return await func(call, state)

    return wrapper
