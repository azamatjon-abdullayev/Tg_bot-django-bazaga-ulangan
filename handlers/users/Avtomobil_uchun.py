from aiogram import types
from . import tarjima_bot_uchun
from loader import dp,bot


# Echo bot
@dp.message_handler(text="shina")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/19"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: Shina\n'
                                                                    'Narxi: 460 000ming som\n')
@dp.message_handler(text="bufer")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/17"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: Bufer\n'
                                                                    'Narxi: 500 000ming som\n')
@dp.message_handler(text="tashqi_tomoni")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/7"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: Mashina tashqi tomoni uchun komplekt\n'
                                                                    'Narxi: 1 950 000ming som\n')
@dp.message_handler(text="ichki_tomoni")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/16"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi:  Mashina ichki tomoni uchun komplekt\n'
                                                                    'Narxi: 560 000ming som\n')


@dp.message_handler(text="Wedga")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/19"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='210$')
@dp.message_handler(text="Buffer")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/17"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="125$")
@dp.message_handler(text="External-side")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/7"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="1150$")
@dp.message_handler(text="Inner-side")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/16"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="1640$")


@dp.message_handler(text="щина")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/c/1613027257/18"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="460$")
@dp.message_handler(text="Буфер")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/17"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="350$")
@dp.message_handler(text="внещная")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/7"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="1150$")
@dp.message_handler(text="Внутренные")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/16"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="1940$")

