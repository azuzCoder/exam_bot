from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage

BOT_TOKEN = 'BOT_TOKEN'

bot = Bot(token=BOT_TOKEN)
storage = MongoStorage(db_name='exam_bot_db')
dp = Dispatcher(bot=bot, storage=storage)
