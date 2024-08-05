from aiogram import types
from aiogram import Router
from aiogram.filters import Command
from aiogram.types.callback_query import CallbackQuery

from data.texts.start_message import text as start_text
from data.texts.about import text as about_text


start_router = Router()

@start_router.message(Command('start'))
async def start(message: types.Message):
    text = start_text
    await message.answer(text=text)

