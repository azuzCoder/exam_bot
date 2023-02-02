from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from bot.middlewares.config import dp
from bot.middlewares.states import UserInfoStateGroup


@dp.message_handler(commands=['cancel'], state='*')
async def cancel(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    explaining = 'Hi welcome to IDU\'s exam bot!'
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Registration', callback_data='register'))

    await message.answer(text=explaining, reply_markup=keyboard)


@dp.callback_query_handler(Text(equals='register', ignore_case=True))
async def start_register(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await UserInfoStateGroup.first()

    await callback.message.answer(text='Enter your F.I.SH.\nExample: Aliyev Ali Aliyevich')
