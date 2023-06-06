from aiogram import Dispatcher
from aiogram.types import ContentTypes

from utils.decorators.reg_decorator import auth_user_message
from . import dialogue


async def register_dialogue_handlers(dp: Dispatcher):
    dp.register_message_handler(auth_user_message(dialogue.dialogue_stop_message_handler), commands=['stop'])
    dp.register_message_handler(auth_user_message(dialogue.dialogue_next_message_handler), commands=['next'])
    dp.register_message_handler(auth_user_message(dialogue.dialogue_search_stop_handler), commands=['search_stop'])
    dp.register_message_handler(auth_user_message(dialogue.dialogue_process_message_handler), content_types=ContentTypes.TEXT)
    dp.register_message_handler(auth_user_message(dialogue.dialogue_process_send_video), content_types=ContentTypes.VIDEO)
    dp.register_message_handler(auth_user_message(dialogue.dialogue_process_send_photo), content_types=ContentTypes.PHOTO)
    dp.register_message_handler(auth_user_message(dialogue.dialogue_process_send_audio), content_types=ContentTypes.VOICE)
    dp.register_message_handler(auth_user_message(dialogue.dialogue_process_send_video_note), content_types=ContentTypes.VIDEO_NOTE)
    dp.register_message_handler(auth_user_message(dialogue.dialogue_process_send_sticker), content_types=ContentTypes.STICKER)
    dp.register_message_handler(auth_user_message(dialogue.dialogue_process_send_document), content_types=ContentTypes.DOCUMENT)
