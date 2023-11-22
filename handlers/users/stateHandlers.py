from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(commands='xarid')
async def xarid_state_handler(msg: types.Message, state: FSMContext):
    await state.set_state('xarid_state')
    await msg.answer("Mahsulot tanlang: ")


@dp.message_handler(state='xarid_state')
async def state_answer(msg: types.Message, state: FSMContext):
    await msg.answer("Mahsulot savatga qo'shildi!")
    await state.finish()
