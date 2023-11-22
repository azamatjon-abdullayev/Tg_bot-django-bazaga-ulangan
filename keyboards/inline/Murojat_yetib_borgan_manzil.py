from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

yuborish_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Siz yuborgan malumot bu kanalning bosh admin sahifasiga yuborildi"),
        ],
        [
            KeyboardButton(text='Yordam_olish_menyusiga_qaytish')
        ]
    ],
    resize_keyboard=True
)