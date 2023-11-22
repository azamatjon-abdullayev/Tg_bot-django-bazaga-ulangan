from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


mini_tehnikalar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='kompyuterlar'),
            KeyboardButton(text='uy_jihozlari'),
        ],
        [
            KeyboardButton(text='pilesoslar'),
            KeyboardButton(text='mashinalar'),
        ],
        [
            KeyboardButton(text='maxsus_mashinalar')
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)
mini_tehnikalar_buttons_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Komputers'),
            KeyboardButton(text='Home-appliances'),
        ],
        [
            KeyboardButton(text='Pilesos'),
            KeyboardButton(text='Cars'),
        ],
        [
            KeyboardButton(text='special_cars')
        ],
        [
            KeyboardButton(text='Back')
        ]
    ],
    resize_keyboard=True
)

mini_tehnikalar_buttons_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Комрйутеры'),
            KeyboardButton(text='техника'),
        ],
        [
            KeyboardButton(text='пилесосы'),
            KeyboardButton(text='Мащины'),
        ],
        [
            KeyboardButton(text='спеч_техникы')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)

