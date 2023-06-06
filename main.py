from aiogram.utils import executor
from aiogram import types, Dispatcher

from loader import dp

from modules.dialogue.reg_handlers import register_dialogue_handlers
from modules.register.reg_handlers import register_reg_user_handlers
from modules.search.reg_handlers import register_search_handlers


async def on_startup(dispatcher: Dispatcher):
    await set_command_handler(dispatcher)
    await register_handlers(dispatcher)


async def register_handlers(dispatcher: Dispatcher):
    await register_reg_user_handlers(dispatcher)
    await register_search_handlers(dispatcher)
    await register_dialogue_handlers(dispatcher)


async def set_command_handler(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands([
        types.BotCommand("stats", "📈 Статистика"),
        types.BotCommand("profile", "👤 Мой профиль"),
        types.BotCommand('search', "🔎 Поиск собеседника"),
        types.BotCommand('search_stop', "⭕️ Остановить поиск"),
        types.BotCommand('next', "🗣 Найти другого собеседника"),
        types.BotCommand('stop', "❌ Прекратить общение"),
    ])


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
