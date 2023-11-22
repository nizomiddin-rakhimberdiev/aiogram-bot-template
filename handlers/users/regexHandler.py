from aiogram import types
from aiogram.dispatcher.filters import Regexp

from loader import dp

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_REGEX = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
COMMAND_EMAIL_REGEX = r"/email:" + EMAIL_REGEX

@dp.message_handler(Regexp(EMAIL_REGEX))
async def email_regex_handler(message: types.Message):
    await message.answer('Email qabul qilindi!')


@dp.message_handler(Regexp(PHONE_REGEX))
async def email_regex_handler(message: types.Message):
    await message.answer('Telefon raqami qabul qilindi!')


@dp.message_handler(regexp_commands=[COMMAND_EMAIL_REGEX])
async def email_regex_handler(message: types.Message):
    await message.answer('Emailingiz qabul qilindi!')
