import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from aiogram import executor, types

from bot.middlewares.config import dp, bot
from bot.middlewares.states import UploadSolutionsStateGroup


from bot.handlers.admin import start_handler
from bot.handlers.user import start_handler, user_info_handler, material_handler

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
