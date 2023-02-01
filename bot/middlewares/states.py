from aiogram.dispatcher.filters.state import State, StatesGroup


class UserInfoStateGroup(StatesGroup):
    full_name = State()
    phone_number = State()
    address = State()
    passport_number = State()
    passport_image = State()

    lang = State()


class UploadSolutionsStateGroup(StatesGroup):
    upload_files = State()
