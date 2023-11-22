from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp


@dp.message_handler(hashtags='money')
async def changeLanguage(message: types.Message):
    text = "Yee, Akang kuchaydi uje!"
    await message.answer(text)


@dp.message_handler(cashtags=['usd', 'eur'])
async def cashtag_handler(message: types.Message):
    await message.answer("Sizda 1412421424$ bor")