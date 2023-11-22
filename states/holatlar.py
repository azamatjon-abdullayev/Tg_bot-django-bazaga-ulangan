from aiogram.dispatcher.filters.state import State,StatesGroup

class Murojat(StatesGroup):

    ism = State()
    familiya = State()
    yosh = State()
    telefon_raqam = State()
    murojat = State()
    tasdiqlash = State()