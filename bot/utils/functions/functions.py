import datetime as dt
from pytz import timezone

from aiogram import types


tz=timezone('Europe/Moscow')

async def delete_message(message: types.Message):
    delta = abs(dt.datetime.now(tz) - message.date)
    access = 2 - delta.seconds/(3600*24) - delta.days
    if access > 0:
        await message.delete()
    else:
        await message.edit_text('Удалено')
