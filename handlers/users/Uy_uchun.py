from aiogram import types
from . import tarjima_bot_uchun
from loader import dp, bot


# Echo bot
@dp.message_handler(text="stol_stul")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/10?single"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: stol_stul\n'
                                                                    'Narxi: 500 000ming som\n')
@dp.message_handler(text="oziq_ovqat")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/9"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: oziq_ovqat toplam\n'
                                                                    'Narxi: 700 000ming som\n')
@dp.message_handler(text="tehnikalar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/5"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: tehnika\n'
                                                                    'Narxi: 50000$\n')
@dp.message_handler(text="qoshimcha_jihozlar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/8"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: qoshimcha jihozlar\n'
                                                                    'Narxi: 3000$\n')


@dp.message_handler(text="table-chair")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/10"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="25$")
@dp.message_handler(text="fast-food")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/9"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="30$")
@dp.message_handler(text="technics")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/5"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="100000$")
@dp.message_handler(text="Added-devices")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/8"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="36000$")


@dp.message_handler(text="стол_стул")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/10"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="25$")
@dp.message_handler(text="ритание")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/9"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="50$")
@dp.message_handler(text="техникы")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/5"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="80000$")
@dp.message_handler(text="доролнителные")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/8"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="75000$")