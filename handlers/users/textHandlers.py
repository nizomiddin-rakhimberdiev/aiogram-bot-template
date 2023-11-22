from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text(contains='Assalamu', ignore_case=True))
@dp.message_handler(Text(equals='Assalamu alaykum', ignore_case=True))
async def text_handler(message: types.Message):
    await message.answer("Va alaykum assalam")