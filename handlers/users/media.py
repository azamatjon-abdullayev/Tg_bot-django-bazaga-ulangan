from aiogram import types
from . import tarjima_bot_uchun
from loader import dp
from aiogram.types import ContentType


# Echo bot
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_echo(message: types.Message):
    await message.document.download()
    await message.answer(text="Dokument saqlab olindi")

@dp.message_handler(content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message):
    await message.video.download()
    await message.answer(text="Video saqlab olindi")

@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[1].download()
    await message.answer(text="Rasm saqlab olindi")

@dp.message_handler(content_types=ContentType.AUDIO)
async def bot_echo(message: types.Message):
    await message.audio.download()
    await message.answer(text="Audio saqlab olindi")

@dp.message_handler(content_types=ContentType.ANIMATION)
async def bot_echo(message: types.Message):
    await message.animation.download()
    await message.answer(text="Animatsiya saqlab olindi")

@dp.message_handler(content_types=ContentType.GAME)
async def bot_echo(message: types.Message):
    await message.game[1].download()
    await message.answer(text="O'yin saqlab olindi")