from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

yordam_olish_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Murojat_yetib_borgan_manzil"),
            KeyboardButton(text="Murojat_qilish_uchun_misol"),
        ],
        [
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard = True
)