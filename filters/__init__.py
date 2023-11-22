from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from . kanal_uchun import Kanal
from . guruh_uchun import Guruh
from . user_uchun import Shaxsiy

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(Guruh)
    dp.filters_factory.bind(Kanal)
    dp.filters_factory.bind(Shaxsiy)

