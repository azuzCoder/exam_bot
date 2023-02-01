from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from bot.middlewares.config import dp
from bot.middlewares.states import UserInfoStateGroup


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    explaining = 'Assalomu alaykum IDUning imtihon topshirish uchun mo`ljallangan botiga xush kelibsiz!'
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Ro`yhatdan o`tish', callback_data='register'))

    await message.answer(text=explaining, reply_markup=keyboard)


@dp.callback_query_handler(Text(equals='register', ignore_case=True))
async def start_register(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await UserInfoStateGroup.first()

    await callback.message.answer(text='F.I.SH ni kiritish:')
