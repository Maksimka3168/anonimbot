from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

bot_method = Bot(config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot_method, storage=MemoryStorage())
