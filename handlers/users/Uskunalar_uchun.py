from aiogram import types
from . import tarjima_bot_uchun
from loader import dp, bot


# Echo bot
@dp.message_handler(text="zal_uchun")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/3"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: zal uchun tehnika\n'
                                                                    'Narxi: 2500$\n')
@dp.message_handler(text="uy_uchun")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/2"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: uy uchun tehnika\n'
                                                                    'Narxi: 1200$\n')
@dp.message_handler(text="shaxsiy")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/4"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: shahsiy tehnika\n'
                                                                    'Narxi: 750$\n')
@dp.message_handler(text="maxsus_trenajorlar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/6"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: mahsus trenajorlar\n'
                                                                    'Narxi: 5000$\n')


@dp.message_handler(text="for_deceitiful")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/3"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="2000$")
@dp.message_handler(text="for_home")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/2"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="1000$")
@dp.message_handler(text="Individual")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/4"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="700$")
@dp.message_handler(text="special_trainer")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/6"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="3000$")


@dp.message_handler(text="для_зала")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/3"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="2000$")
@dp.message_handler(text="для_дома")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/2"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="1000$")
@dp.message_handler(text="личные")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/4"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="4000$")
@dp.message_handler(text="среч_тренажоры")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/6"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="5000$")