from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.tillar import tillar_buttons
from states.holatlar import Murojat
from . import tarjima_bot_uchun
from loader import dp, bot
from keyboards.default.tasdiqlash import tasdiqlash_tugmalari

# Echo bot
@dp.message_handler(text='Murojat qilish')
async def bot_echo(message: types.Message):

    await message.answer(text='Ismni kiriting ')
    await Murojat.ism.set()


@dp.message_handler(state=Murojat.ism)
async def bot_echo(message: types.Message, state:FSMContext):
    ism = message.text
    await state.update_data({'name':ism})
    await message.answer(text="Familiyani kiriting")

    await Murojat.familiya.set()

@dp.message_handler(state=Murojat.familiya)
async def bot_echo(message: types.Message, state:FSMContext):
    ism = message.text
    await state.update_data({'name':ism})
    await message.answer(text="yoshni kiriting")

    await Murojat.yosh.set()

@dp.message_handler(state=Murojat.yosh)
async def bot_echo(message: types.Message, state:FSMContext):
    ism = message.text
    await state.update_data({'name':ism})
    await message.answer(text="telefon raqam kiriting")

    await Murojat.telefon_raqam.set()



@dp.message_handler(state=Murojat.telefon_raqam)
async def bot_echo(message: types.Message, state:FSMContext):
    tel = message.text
    if tel.isdigit():
        await state.update_data({'name':tel})
        await message.answer(text="Murojatni kiriting")
        await Murojat.murojat.set()
    else:
        await message.answer(text="Bunday raqam mavjud emas.Qaytadan raqamni kiriting")
        await Murojat.telefon_raqam.set()

@dp.message_handler(state=Murojat.murojat)
async def bot_echo(message: types.Message, state:FSMContext):
    ism = message.text
    await state.update_data({'name':ism})
    foydalanuvchi_malumotlari =await state.get_data()
    user_name = foydalanuvchi_malumotlari.get('name')
    familya = foydalanuvchi_malumotlari.get('name')
    yosh = foydalanuvchi_malumotlari.get('name')
    telefon_raqami = foydalanuvchi_malumotlari.get('name')
    ariza = foydalanuvchi_malumotlari.get('name')

    matn = f"     ISM : {user_name} \n" \
           f"     Familiya : {familya} \n"\
           f"     Yosh : {yosh} \n"\
           f"     Telefoni : {telefon_raqami}\n"\
           f"     Murojat : {ariza}"\

    await message.answer(text=matn,reply_markup=tasdiqlash_tugmalari)
    await Murojat.tasdiqlash.set()

@dp.message_handler(text='Tasdiqlash',state=Murojat.tasdiqlash)
async def bot_echo(message: types.Message, state:FSMContext):
    nick_name = message.from_user.username
    foydalanuvchi_malumotlari = await state.get_data()
    user_name = foydalanuvchi_malumotlari.get('name')
    familya = foydalanuvchi_malumotlari.get('name')
    yosh = foydalanuvchi_malumotlari.get('name')
    telefon_raqami = foydalanuvchi_malumotlari.get('name')
    ariza = foydalanuvchi_malumotlari.get('name')


    matn = f"     ISM : {user_name} \n" \
           f"     Familiya : {familya} \n" \
           f"     Yosh : {yosh} \n" \
           f"     Telefoni : {telefon_raqami}\n" \
           f"     Murojat : {ariza} \n" \
           f"Ushbu foydalanuvchi habar yubordi {nick_name}"\

    await bot.send_message(chat_id='195041374', text=matn)
    await message.answer(text='Botga xush kelibsiz',reply_markup=tillar_buttons)
    await message.answer(text="kia",reply_markup=ReplyKeyboardRemove())
    await state.finish()

@dp.message_handler(text='Bekor qilish',state=Murojat.tasdiqlash)
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bekor qilindi' ,reply_markup=tillar_buttons)
    await message.answer(text="kia",reply_markup=ReplyKeyboardRemove())
    await state.finish()




