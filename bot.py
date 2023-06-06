from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor\

TOKEN = '12345'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)