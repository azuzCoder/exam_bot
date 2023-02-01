from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage

BOT_TOKEN = '5505071713:AAHEq4b8BSycSzpumbKzm25H0_3XBjjyCPc'

bot = Bot(token=BOT_TOKEN)
storage = MongoStorage(db_name='exam_bot_db')
dp = Dispatcher(bot=bot, storage=storage)
