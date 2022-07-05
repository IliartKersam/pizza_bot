from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = '5031871873:AAE6gTk7vLBngVmHlpg-rxdDwFNk-DLcM6w'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)