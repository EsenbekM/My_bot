#!venv/bin/python
import logging
from typing import TextIO
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import message_id, user
from aiogram.types.message import Message
from mat import *
from filters import Is_Admin_Filter
from asyncio import sleep
import random
import markups as mp
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token="1977948311:AAHySwxcRlMPsMmVlvXpBeghXLcMf3yrBkw")
GROUP_ID = -1001269417782

# Диспетчер для бота
dp = Dispatcher(bot)

# фильтры для кнопок
dp.filters_factory.bind(Is_Admin_Filter)

# Функция бан
@dp.message_handler(is_admin = True, commands=["ban"])
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    await message.delete()
    await message.bot.kick_chat_member(chat_id=GROUP_ID,user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply(f"Пользователь {message.reply_to_message.from_user.full_name} был забанен по воле Эсенбека")

# Функция для удалении сообщений о присоеденений
@dp.message_handler(chat_id=GROUP_ID, content_types=["new_chat_members"])
async def on_user_join(message: types.Message):
    await message.delete()

# Функция разбан
@dp.message_handler(is_admin = True, commands=["unban"])
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    await message.delete()
    await message.bot.unban_chat_member(chat_id=GROUP_ID,user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply(f"Пользователь {message.reply_to_message.from_user.full_name} был раззабанен по воле Эсенбека")



# Функция для вызова игр
@dp.message_handler(commands=["game"])
async def games_bot(message: types.Message):
    await bot.send_message(GROUP_ID, "ИГРЫ", reply_markup=mp.games)


# Функция с откликом на игру кости
@dp.callback_query_handler(text="bones")
async def play_bones(mesage: types.Message):
    await bot.delete_message(GROUP_ID, mesage.message.message_id)
    await bot.send_message(GROUP_ID, f"{mesage.from_user.first_name}   VS   BOT")
    await sleep(1)

    await bot.send_message(GROUP_ID, 'Кость БОТА')
    bot_data = await bot.send_dice(GROUP_ID)
    bot_data = bot_data['dice']['value']
    await sleep(5)
    
    await bot.send_message(GROUP_ID, f"Кость {mesage.from_user.first_name}")
    user_data = await bot.send_dice(GROUP_ID)
    user_data = user_data['dice']['value']
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(GROUP_ID, 'Ты проиграл ЛОШОК )')
    elif user_data > bot_data:
        await bot.send_message(GROUP_ID, 'Ты выиграл БАЗАР ЖОК!')
    else:
        await bot.send_message(GROUP_ID, 'НИЧЬЯ НАХОЙ!')

# Функция с откликом на игру камень ножницы бумага
@dp.callback_query_handler(text="kmb")
async def kamen_bum(message: types.Message):
    await bot.delete_message(GROUP_ID, message.message.message_id)
    await bot.send_message(GROUP_ID, f"{message.from_user.first_name} VS BOT\n Выбирай:", reply_markup=mp.kam_noj_bum)
# медоды для игры камень ножницы бумага
@dp.callback_query_handler(text="kamen")
async def kamen_fun(message: types.Message):

    await bot.delete_message(GROUP_ID, message.message.message_id)

    if bot_play[random.randint(0,2)] == bot_play[0]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[0]}\nТы выбрал ✊🏻\nНИЧЬЯ НАХОЙ!')
    elif bot_play[random.randint(0,2)] == bot_play[1]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[1]}\nТы выбрал ✊🏻\nТы выиграл БАЗАР ЖОК!')
    elif bot_play[random.randint(0,2)] == bot_play[2]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[2]}\nТы выбрал ✊🏻\nТы проиграл ЛОШОК )')
    
@dp.callback_query_handler(text="nojnicy")
async def nojnicy_fun(message: types.Message):

    await bot.delete_message(GROUP_ID, message.message.message_id)

    if bot_play[random.randint(0,2)] == bot_play[1]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[1]}\nТы выбрал ✌🏻\nНИЧЬЯ НАХОЙ!')
    elif bot_play[random.randint(0,2)] == bot_play[2]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[2]}\nТы выбрал ✌🏻\nТы выиграл БАЗАР ЖОК!')
    elif bot_play[random.randint(0,2)] == bot_play[0]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[0]}\nТы выбрал ✌🏻\nТы проиграл ЛОШОК )')

@dp.callback_query_handler(text="bumaga")
async def bumaga_fun(message: types.Message):

    await bot.delete_message(GROUP_ID, message.message.message_id)

    if bot_play[random.randint(0,2)] == bot_play[2]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[2]}\nТы выбрал ✋🏻\nНИЧЬЯ НАХОЙ!')
    elif bot_play[random.randint(0,2)] == bot_play[0]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[0]}\nТы выбрал ✋🏻\nТы выиграл БАЗАР ЖОК!')
    elif bot_play[random.randint(0,2)] == bot_play[1]:
        await bot.send_message(GROUP_ID, f'Бот выбрал {bot_play[1]}\nТы выбрал ✊🏻\nТы проиграл ЛОШОК )')


# Фильтры и функции модератора для чатов
@dp.message_handler()
async def loxi(message: types.Message):
    for i in list3:
        if i in message.text.lower():
            await message.reply("Нет он лох!")
        else:
            pass
    for i in list2:
        if i in message.text.lower():
            await message.reply(f"Ты прав! {i}")
        else:
            pass
    for i in list1:
        if i in message.text.lower():
            await message.delete()
            await message.answer(f"{message.from_user.full_name} Не матерись! Сам(a) ты {i}")
        else:
            pass
    for i in hello:
        if i in message.text.lower():
            await message.reply('Здорова заебал!')




if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
