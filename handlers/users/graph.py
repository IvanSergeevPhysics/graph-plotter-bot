from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, bot
from states import Plot

import os
import pandas as pd
import matplotlib.pyplot as plt


def getData(path):
    df = pd.read_csv(path, sep=" ", names=["x", "y"])
    return list(df.x), list(df.y)


def plotGraph(x, y):
    plt.plot(x, y)
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(fname='result.png', format='png')
    plt.cla()


def getParams(text):
    func, a, b = text.split()
    return func, float(a), float(b)


def result(text):
    func, a, b = getParams(text)

    cmd = f'rpn.exe {a} {b} {func}'
    os.system(cmd)
    x, y = getData("nodes.txt")
    plotGraph(x, y)


@dp.message_handler(Command('plot'))
async def start_plot(message: types.Message):
    await message.answer(text=f"Enter the function and limits in format 'f(x) left_lim right_lim'")
    await Plot.plot.set()


@dp.message_handler(state=Plot.plot)
async def plot(message: types.Message, state: FSMContext):
    result(message.text)

    await bot.send_photo(message.chat.id, types.InputFile('result.png'))

    os.remove('result.png')
    await state.finish()
