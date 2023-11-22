from aiogram import types
from . import tarjima_bot_uchun
from loader import dp,bot


# Echo bot
@dp.message_handler(text="kompyuterlar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/15"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: kompyuter\n'
                                                                    'Narxi: 800$\n')
@dp.message_handler(text="uy_jihozlari")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/14"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: uy jihozlari komplekt\n'
                                                                    'Narxi: 50 000$\n')
@dp.message_handler(text="pilesoslar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/13"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: pilesos\n'
                                                                    'Narxi: 2 500 000 ming som\n')
@dp.message_handler(text="mashinalar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/12"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: kir yuvish mashinasi\n'
                                                                    'Narxi: 3 500 000 ming som\n')
@dp.message_handler(text="maxsus_mashinalar")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/11"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption='Mahsulot nomi: mahsus mashina\n'
                                                                    'Narxi: 1000$\n')


@dp.message_handler(text="Komputers")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/15"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="800$")
@dp.message_handler(text="Home-appliances")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/14"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="1000$")
@dp.message_handler(text="Pilesos")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/13"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="300$")
@dp.message_handler(text="Cars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/12"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="200$")
@dp.message_handler(text="special_cars")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/11"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="700$")


@dp.message_handler(text="Комрйутеры")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/15"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="800$")
@dp.message_handler(text="техника")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/14"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="700$")
@dp.message_handler(text="пилесосы")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/13"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="200$")
@dp.message_handler(text="Мащины")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/12"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="400$")
@dp.message_handler(text="спеч_техникы")
async def bot_echo(message: types.Message):
    user_id = message.from_user.id
    rasm_manzili = "https://t.me/azmatzor2/11"
    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="900$")