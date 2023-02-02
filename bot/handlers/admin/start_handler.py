from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.middlewares.config import dp
from bot.middlewares.filters import is_admin


@dp.message_handler(is_admin, commands=['start'])
async def start(message: types.Message):
    await message.answer('Siz adminsiz!')
