from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(commands='change_photo', is_chat_admin=True)
async def admin_handler(message: types.Message):
    await message.answer("Rasmni almashtiramizmi?")
   