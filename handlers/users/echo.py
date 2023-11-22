from aiogram import types
from . import tarjima_bot_uchun
from loader import dp
from filters.user_uchun import Shaxsiy

# Echo bot
@dp.message_handler(Shaxsiy(),state=None)
async def bot_echo(message: types.Message):
    await message.answer(message.text)
