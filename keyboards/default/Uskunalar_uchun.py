from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


uskuna_uchun_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='zal_uchun'),
            KeyboardButton(text='uy_uchun'),
        ],
        [
            KeyboardButton(text='shaxsiy'),
            KeyboardButton(text='maxsus_trenajorlar'),
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)
uskuna_uchun_button_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='for_deceitiful'),
            KeyboardButton(text='for_home'),
        ],
        [
            KeyboardButton(text='Individual'),
            KeyboardButton(text='special_trainer'),
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)
uskuna_uchun_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='для_зала'),
            KeyboardButton(text='для_дома'),
        ],
        [
            KeyboardButton(text='личные'),
            KeyboardButton(text='среч_тренажоры'),
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)

