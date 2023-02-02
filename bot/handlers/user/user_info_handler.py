import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import bold

from bot.middlewares.config import dp
from bot.middlewares.states import UserInfoStateGroup
from bot.handlers.user.material_handler import send_list_lang
from bot.middlewares import api


@dp.message_handler(state=UserInfoStateGroup.full_name, content_types=types.ContentType.ANY)
async def get_full_name(message: types.Message, state: FSMContext):
    if message.text and checking_full_name(message.text):
        await state.update_data(full_name=message.text)
        await UserInfoStateGroup.next()
        await message.answer('Enter your phone number\n' + 'Example: +998912345678')
        return
    await message.answer('F.I.O is incorrect!')


@dp.message_handler(state=UserInfoStateGroup.phone_number, content_types=types.ContentType.ANY)
async def get_phone_number(message: types.Message, state: FSMContext):
    if message.text and checking_phone_number(message.text):
        await state.update_data(phone_number=message.text)
        await UserInfoStateGroup.next()
        await message.answer('Enter your home address:')
        return
    await message.answer('Enter correct number!!!\n' + 'Example: +998912345678')


@dp.message_handler(state=UserInfoStateGroup.address, content_types=types.ContentType.ANY)
async def get_address(message: types.Message, state: FSMContext):
    if message.text:
        await state.update_data(address=message.text)
        await UserInfoStateGroup.next()
        await message.answer('Enter your passport seria and number\n' + 'Example: AD1234567')
        return
    await message.answer('Enter text only!!!')


@dp.message_handler(state=UserInfoStateGroup.passport_number, content_types=types.ContentType.ANY)
async def get_passport_number(message: types.Message, state: FSMContext):
    if message.text and checking_passport_number(message.text):
        await state.update_data(passport_number=message.text)
        await UserInfoStateGroup.next()
        await message.answer('Send a copy of passport (as image or pdf).')
        return
    await message.answer('Passport number is incorrect!')


@dp.message_handler(state=UserInfoStateGroup.passport_image, content_types=types.ContentType.ANY)
async def get_passport_image(message: types.Message, state: FSMContext):
    if not (message.photo or message.document.mime_base == 'image' or message.document.mime_subtype == 'pdf'):
        await message.answer('Only image or pdf!!!')
        return
    file_id = get_file_id(message)
    await state.update_data(passport_image=file_id)
    await state.update_data(from_id=message.from_id)

    await UserInfoStateGroup.next()
    await send_list_lang(message)


def get_file_id(message: types.Message):
    if message.photo:
        return message.photo[-1].file_id
    return message.document.file_id


def checking_full_name(name: str):
    pieces = list(map(str, name.split()))
    if len(pieces) == 3:
        return True
    return False


def checking_phone_number(number: str):
    pattern = "^[+][9][9][8][0-9]{9}$"
    regex = re.compile(pattern)
    span = regex.match(number)
    if span is None:
        return False
    span = span.span()
    if (0, len(number)) == span:
        return True
    return False


def checking_passport_number(passport: str):
    if len(passport) != 9:
        return False
    seria = passport[:2]
    number = passport[2:]
    if seria.isalpha() and number.isdigit():
        return seria.upper() + number
    return False
