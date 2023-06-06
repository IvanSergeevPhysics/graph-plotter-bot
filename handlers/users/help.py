from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List of commands: ",
            "/start - Start using bot",
            "/help - Get list of commands",
            "/plot - Get graph of function")

    await message.answer("\n".join(text))

