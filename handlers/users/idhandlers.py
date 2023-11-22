from aiogram import types

from loader import dp

SUPERUSERS = [2424224, 3123131]
BLACKLiST = [42313442, 5324244]


@dp.message_handler(chat_id=SUPERUSERS, commands='start')
async def id_filter_handler(message: types.Message):
    await message.answer("Xush kelibsiz, SuperUSER!")
