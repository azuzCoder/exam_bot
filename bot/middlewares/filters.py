from aiogram import types

from bot.middlewares import api


def is_admin(message: types.Message):
    if api.get(message.from_id, api.get_admin_by_from_id):
        return True
    return False
