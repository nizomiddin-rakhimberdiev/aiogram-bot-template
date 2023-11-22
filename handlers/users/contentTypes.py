from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(message: types.Message):
    await message.answer('Bu nima rasm?')


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def photo_handler(message: types.Message):
    await message.answer('Yaxshi eshitilmayapdi')


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def photo_handler(message: types.Message):
    await message.answer('Bu nima fayl?')


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def photo_handler(message: types.Message):
    await message.answer('Bu qayerni lokatsiyasi?')
