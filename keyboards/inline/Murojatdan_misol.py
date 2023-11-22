from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

murojat_misol_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Murojatdan_misol\n"
                                      "Ismingizni kiriting : ism kiritish %%%%%%%\n"
                                      "Familiyani kiriting : familiya kiritish %%%%%%%%\n"
                                      "Yosh kiriting : yosh kiritish %%%%%%%%%\n"
                                      "Telefon kiriting : Telefon kiritish %%%%%%%%%\n"
                                      "Malumot joyiga o'zingiz haqida malumot kiritish",callback_data='misol1'),
        ],
        [
            KeyboardButton(text='Yordam_olish_menyusiga_qaytish')
        ]
    ],
    resize_keyboard=True
)