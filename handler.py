from typing import Text
from bot import bot, dp

from aiogram.types import Massage, chat
from config import admin_id

async def send_to_admin(dp):
    await bot.send_massage(chat_id=admin_id, Text='Bot started!')