import random

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from config.settings import MEDIA_ROOT
from bot.middlewares.config import dp, bot
from bot.middlewares import api
from bot.middlewares.states import UserInfoStateGroup, UploadSolutionsStateGroup


def check_lang(callback: types.CallbackQuery):
    if callback.data in ('uz', 'ru', 'en'):
        return True
    return False


async def send_list_lang(message: types.Message):
    langs = types.InlineKeyboardMarkup()
    langs.add(types.InlineKeyboardButton(text='O`zbek', callback_data='uz'),
              types.InlineKeyboardButton(text='English', callback_data='en'),
              types.InlineKeyboardButton(text='Русский', callback_data='ru'))

    await message.answer('Select the language for the math exam.', reply_markup=langs)


@dp.callback_query_handler(check_lang, state=UserInfoStateGroup.lang)
async def get_lang(callback: types.CallbackQuery, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Upload solution')
    await callback.message.answer_document(types.InputFile(MEDIA_ROOT / 'pdfs' / ('math_' + callback.data + '.pdf')),
                                           caption='Your exam material', reply_markup=keyboard)
    await callback.message.answer('You can upload your solutions as pdf file. Prepare your solution.')
    await callback.message.delete_reply_markup()
    await state.reset_state(with_data=False)


@dp.message_handler(Text(equals='Upload solution', ignore_case=True))
async def starting_upload(message: types.Message):
    await UploadSolutionsStateGroup.first()
    await message.answer('We know You have done everything well. '
                         'Now you can upload your solutions. Please send as pdf file',
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=UploadSolutionsStateGroup.upload_files, content_types=types.ContentType.ANY)
async def upload_solution(message: types.Message, state: FSMContext):
    print(message)
    if not (message.document and message.document.mime_subtype == 'pdf'):
        await message.answer('You need to upload pdf file.')
        return
    solution = message.document.file_id
    await state.update_data(solution=solution)
    # await message.document.download(destination_file=MEDIA_ROOT / 'solutions' /(str(trf_code()) + '.pdf'))
    data = await state.get_data()
    user = api.post(api.add_user, data)
    await send_admins(user)

    await message.answer('Thank you for your answers. We try to inform about your score as soon as possible.')
    await state.reset_state()


def trf_code():
    return random.randint(1000000, 9999999)


async def send_admins(user):
    admins = api.get(addr=api.list_admins)
    for admin in admins:
        await bot.send_document(admin['from_id'], user['solution'],
                                caption=f'Full name:{user["full_name"]}\nPhone number:{user["phone_number"]}')
