from aiogram import types
from filters.guruh_uchun import Guruh
from loader import dp


# Echo bot
@dp.message_handler(Guruh(),commands='start')
async def bot_echo(message: types.Message):
    await message.answer(text='Guruhga hush kelibsiz')

@dp.message_handler(Guruh(),text='salom')
async def bot_echo(message: types.Message):
    username =message.from_user.username
    await message.answer(text=f'Salom bu guruh xush kelibsiz {username}')