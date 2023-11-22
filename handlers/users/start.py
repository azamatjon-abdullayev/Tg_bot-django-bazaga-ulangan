from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery


from keyboards.default.supermarket import supermarket_buttons
from keyboards.default.supermarket import supermarket_buttons_en
from keyboards.default.supermarket import supermarket_buttons_ru
from keyboards.default.Mini_tehnikalar import mini_tehnikalar_buttons
from keyboards.default.Mini_tehnikalar import mini_tehnikalar_buttons_en
from keyboards.default.Mini_tehnikalar import mini_tehnikalar_buttons_ru
from keyboards.default.Uy_uchun import uy_buttons
from keyboards.default.Uy_uchun import uy_buttons_en
from keyboards.default.Uy_uchun import uy_buttons_ru
from keyboards.default.Avtomobil_uchun import avtomobil_buttons
from keyboards.default.Avtomobil_uchun import avtomobil_buttons_en
from keyboards.default.Avtomobil_uchun import avtomobil_buttons_ru
from keyboards.default.Uskunalar_uchun import uskuna_uchun_button
from keyboards.default.Uskunalar_uchun import uskuna_uchun_button_en
from keyboards.default.Uskunalar_uchun import uskuna_uchun_button_ru
from keyboards.inline.Murojat_yetib_borgan_manzil import yuborish_buttons
from keyboards.inline.Murojatdan_misol import murojat_misol_buttons
from keyboards.inline.Yordam_olish_uchun import yordam_olish_buttons
from filters.user_uchun import Shaxsiy
from keyboards.inline.tillar import tillar_buttons
from loader import dp,base,bot


@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    username = message.from_user.username
    user_id = message.from_user.id
    try:
       base.user_qoshish(ism=ism,tg_id=user_id,fam=familya,username=username)
    except Exception as x:
        print(x)
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)


@dp.message_handler(text='Mini_tehnikalar')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring",reply_markup=mini_tehnikalar_buttons)

@dp.message_handler(text='For_technics')
async def bot_start(message: types.Message):
    await message.answer(f"Choose",reply_markup=mini_tehnikalar_buttons_en)

@dp.message_handler(text='Для_техникы')
async def bot_start(message: types.Message):
    await message.answer(f"Выберите",reply_markup=mini_tehnikalar_buttons_ru)


@dp.message_handler(text='Uy_uchun')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring",reply_markup=uy_buttons)

@dp.message_handler(text='For_home')
async def bot_start(message: types.Message):
    await message.answer(f"Choose",reply_markup=uy_buttons_en)

@dp.message_handler(text='Для_дом')
async def bot_start(message: types.Message):
    await message.answer(f"Выберите",reply_markup=uy_buttons_ru)


@dp.message_handler(text='Avtomobil_uchun')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring",reply_markup=avtomobil_buttons)

@dp.message_handler(text='For_car')
async def bot_start(message: types.Message):
    await message.answer(f"Choose",reply_markup=avtomobil_buttons_en)

@dp.message_handler(text='Для_машины')
async def bot_start(message: types.Message):
    await message.answer(f"Выберите",reply_markup=avtomobil_buttons_ru)


@dp.message_handler(text='Uskunalar_uchun')
async def bot_start(message: types.Message):
    await message.answer(f"tanlovni amalga oshiring",reply_markup=uskuna_uchun_button)
@dp.message_handler(text='For_mechanics')
async def bot_start(message: types.Message):
    await message.answer(f"Choose",reply_markup=uskuna_uchun_button_en)
@dp.message_handler(text='Для_инструменты')
async def bot_start(message: types.Message):
    await message.answer(f"Выберите",reply_markup=uskuna_uchun_button_ru)


@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=supermarket_buttons)
@dp.message_handler(text='Back')
async def bot_start(message: types.Message):
    await message.answer(f"Choose, {message.from_user.full_name}!",reply_markup=supermarket_buttons_en)
@dp.message_handler(text='Назад')
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=supermarket_buttons_ru)

@dp.callback_query_handler(text='til1')
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(text=f"tanlovni amalga oshiring",reply_markup=supermarket_buttons)

@dp.callback_query_handler(text='til3')
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(text=f"Choose",reply_markup=supermarket_buttons_en)

@dp.callback_query_handler(text='til2')
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(text=f"Выберите",reply_markup=supermarket_buttons_ru)

@dp.message_handler(text='Yordam_olish')
async def bot_start(message: types.Message):
    await message.answer(f"yordam olish menyusiga xush kelibsiz,",reply_markup=yordam_olish_buttons)

@dp.message_handler(text='Murojat_yetib_borgan_manzil')
async def bot_start(message: types.Message):
    await message.answer(f"Malumotni qabul qiling, ",reply_markup=yuborish_buttons)

@dp.message_handler(text='Murojat_qilish_uchun_misol')
async def bot_start(message: types.Message):
    await message.answer(f"Murojatdan misol tugmasini bosing, !",reply_markup=murojat_misol_buttons)

@dp.message_handler(text='Yordam_olish_menyusiga_qaytish')
async def bot_start(message: types.Message):
    await message.answer(f"Siz yordam olish menyusiga qaytdingiz, {message.from_user.full_name}!",reply_markup=yordam_olish_buttons)

@dp.message_handler(commands='users',chat_id='2016468945')
async def bot_start(message: types.Message):
    soni = base.user_sanash()
    print(soni)
    await message.answer(text=f"Botdan {soni} odam foydalanmoqda")


@dp.message_handler(commands='reklama',chat_id='2016468945')
async def bot_start(message: types.Message):
    userlar = base.barcha_foydalanuvchilarni_tanlash()
    for user in userlar:
        user_id = user[4]
        await bot.send_message(chat_id=user_id,text=f"Bu reklama ")
