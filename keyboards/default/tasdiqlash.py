from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


tasdiqlash_tugmalari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Tasdiqlash'),
            KeyboardButton(text='Bekor qilish'),
        ],
    ],
    resize_keyboard=True
)