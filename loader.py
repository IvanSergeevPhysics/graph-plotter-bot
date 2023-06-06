from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#from data import config

token = '6034563325:AAFGiZBNg_-wONkzwioUQQEb1NSFpS0AAbg'

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
