from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from data import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()
storage = MemoryStorage()
