from aiogram import types
from aiogram import Router
from aiogram.filters import Command

from data.texts import text as start_text


start_router = Router()

@start_router.message(Command['start'])
async def start(message: types.Message):
    text = start_text
    await message.answer(text=text)