from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


avtomobil_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='shina'),
            KeyboardButton(text='bufer'),
        ],
        [
            KeyboardButton(text='tashqi_tomoni'),
            KeyboardButton(text='ichki_tomoni'),
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


avtomobil_buttons_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Wedga'),
            KeyboardButton(text='Buffer'),
        ],
        [
            KeyboardButton(text='External-side'),
            KeyboardButton(text='Inner-side'),
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)
avtomobil_buttons_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='щина'),
            KeyboardButton(text='Буфер'),
        ],
        [
            KeyboardButton(text='внещная'),
            KeyboardButton(text='Внутренные'),
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
