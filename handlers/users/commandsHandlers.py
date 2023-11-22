from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp


@dp.message_handler(Command('til'))
async def changeLanguage(message: types.Message):
    text = "Til o'zgartirildi"
    await message.answer(text)
