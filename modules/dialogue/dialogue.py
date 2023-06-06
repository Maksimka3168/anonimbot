import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from database.db import Database
from loader import bot_method

db = Database("database/db.db")


async def dialogue_search_stop_handler(message: types.Message, state: FSMContext):
    if db.check_available_search_user(message.from_user.id):
        db.delete_companion_user(message.from_user.id)
        await message.answer("Ты успешно прекратил поиск собеседника.")
    else:
        await message.answer("Извини, но ты не в поиске =(")


async def dialogue_next_message_handler(message: types.Message, state: FSMContext):
    user_id_answer = db.check_available_dialogue_user(message.from_user.id)
    if user_id_answer is not None:
        if user_id_answer[0] is not None:
            await bot_method.send_message(chat_id=user_id_answer[0], text="Собеседник покинул чат. "
                                                                          "Твой поиск продолжается, "
                                                                          "используй /stop для остановки")
    db.delete_companion_user(message.from_user.id)
    await message.answer("Ты успешно завершилц общение с собеседником! Ищем тебе нового собеседника!")
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


async def dialogue_stop_message_handler(message: types.Message, state: FSMContext):
    user_id_answer = db.check_available_dialogue_user(message.from_user.id)
    if user_id_answer is not None:
        if user_id_answer[0] is not None:
            await bot_method.send_message(chat_id=user_id_answer[0], text="Собеседник покинул чат. "
                                                                          "Твой поиск продолжается, "
                                                                          "используй /stop для остановки")
    db.delete_companion_user(message.from_user.id)
    await message.answer("Ты успешно завершил общение с собеседником!")


async def dialogue_process_message_handler(message: types.Message, state: FSMContext):
    if db.check_available_talk(message.from_user.id):
        user_id_answer = db.check_available_dialogue_user(message.from_user.id)
        if user_id_answer is not None:
            if user_id_answer[0] is not None:
                await bot_method.send_message(chat_id=user_id_answer[0], text=message.text)
            else:
                await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
                db.delete_companion_user(message.from_user.id)
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
            await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
            db.delete_companion_user(message.from_user.id)
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


async def dialogue_process_send_photo(message: types.Message, state: FSMContext):
    if db.check_available_talk(message.from_user.id):
        user_id_answer = db.check_available_dialogue_user(message.from_user.id)
        if user_id_answer is not None:
            if user_id_answer[0] is not None:
                await bot_method.send_photo(chat_id=user_id_answer[0], photo=message.photo[0].file_id)
            else:
                await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
                db.delete_companion_user(message.from_user.id)
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
            await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
            db.delete_companion_user(message.from_user.id)
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


async def dialogue_process_send_video(message: types.Message, state: FSMContext):
    if db.check_available_talk(message.from_user.id):
        user_id_answer = db.check_available_dialogue_user(message.from_user.id)
        if user_id_answer is not None:
            if user_id_answer[0] is not None:
                await bot_method.send_video(chat_id=user_id_answer[0], video=message.video.file_id)
            else:
                await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
                db.delete_companion_user(message.from_user.id)
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
            await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
            db.delete_companion_user(message.from_user.id)
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


async def dialogue_process_send_audio(message: types.Message, state: FSMContext):
    if db.check_available_talk(message.from_user.id):
        user_id_answer = db.check_available_dialogue_user(message.from_user.id)
        if user_id_answer is not None:
            if user_id_answer[0] is not None:
                await bot_method.send_voice(chat_id=user_id_answer[0], voice=message.voice.file_id)
            else:
                await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
                db.delete_companion_user(message.from_user.id)
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
            await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
            db.delete_companion_user(message.from_user.id)
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


async def dialogue_process_send_video_note(message: types.Message, state: FSMContext):
    if db.check_available_talk(message.from_user.id):
        user_id_answer = db.check_available_dialogue_user(message.from_user.id)
        if user_id_answer is not None:
            if user_id_answer[0] is not None:
                await bot_method.send_video_note(chat_id=user_id_answer[0], video_note=message.video_note.file_id)
            else:
                await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
                db.delete_companion_user(message.from_user.id)
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
            await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
            db.delete_companion_user(message.from_user.id)
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


async def dialogue_process_send_sticker(message: types.Message, state: FSMContext):
    if db.check_available_talk(message.from_user.id):
        user_id_answer = db.check_available_dialogue_user(message.from_user.id)
        if user_id_answer is not None:
            if user_id_answer[0] is not None:
                await bot_method.send_sticker(chat_id=user_id_answer[0], sticker=message.sticker.file_id)
            else:
                await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
                db.delete_companion_user(message.from_user.id)
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
            await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
            db.delete_companion_user(message.from_user.id)
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


async def dialogue_process_send_document(message: types.Message, state: FSMContext):
    if db.check_available_talk(message.from_user.id):
        user_id_answer = db.check_available_dialogue_user(message.from_user.id)
        if user_id_answer is not None:
            if user_id_answer[0] is not None:
                await bot_method.send_document(chat_id=user_id_answer[0], document=message.document.file_id)
            else:
                await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
                db.delete_companion_user(message.from_user.id)
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
            await message.answer("Произошла ошибка! Автоматический поиск следующего собеседника.")
            db.delete_companion_user(message.from_user.id)
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
