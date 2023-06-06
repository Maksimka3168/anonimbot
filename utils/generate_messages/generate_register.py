from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import escape_md


async def generate_message_register_step_1():
    text = f"""
*РЕГИСТРАЦИЯ*

Введи своё псевдоним или настоящее имя 👇
"""
    return text


async def generate_message_register_success():
    text = """
*РЕГИСТРАЦИЯ*

Поздравляю, ты успешно зарегистрировался 👊 Можешь начинать общаться 😁
"""
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Найти собеседника", callback_data="search")
        ]
    ])
    return text, inline_keyboard


async def generator_message_register_message_already(first_name: str):
    text = f"""
*РЕГИСТРАЦИЯ*

{escape_md(first_name)}, ТЫ уже зарегистрирован, можешь *начинать поиск* 😁    
"""
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Найти собеседника", callback_data="search")
        ]
    ])
    return text, inline_keyboard
