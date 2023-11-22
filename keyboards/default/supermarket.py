from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

supermarket_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Avtomobil_uchun'),
            KeyboardButton(text='Uy_uchun'),
        ],
        [
            KeyboardButton(text='Uskunalar_uchun'),
            KeyboardButton(text='Mini_tehnikalar'),
        ],
        [
            KeyboardButton(text='Kontakt',request_contact=True),
            KeyboardButton(text="lokatsiya",request_location=True)
        ],
        [
            KeyboardButton(text='Murojat qilish')
        ],
        [
            KeyboardButton(text='Yordam_olish')
        ]
    ],
    resize_keyboard=True
)
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

supermarket_buttons_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='For_car'),
            KeyboardButton(text='For_home'),
        ],
        [
            KeyboardButton(text='For_mechanics'),
            KeyboardButton(text='For_technics'),
        ],
        [
            KeyboardButton(text='Contact',request_contact=True),
            KeyboardButton(text="Location",request_location=True)
        ]
    ],
    resize_keyboard=True
)
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

supermarket_buttons_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Для_машины'),
            KeyboardButton(text='Для_дом'),
        ],
        [
            KeyboardButton(text='Для_инструменты'),
            KeyboardButton(text='Для_техникы'),
        ],
        [
            KeyboardButton(text='Contact',request_contact=True),
            KeyboardButton(text="Location",request_location=True)
        ]
    ],
    resize_keyboard=True
)

