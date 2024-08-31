from aiogram import Router
from aiogram import F
from aiogram.types.error_event import ErrorEvent
from aiogram.exceptions import (
    DetailedAiogramError
)

import logging



error_router = Router()

@error_router.error()
async def aiogram_error(event: ErrorEvent):
    logging.error(str(event))


@error_router.message(F.photo)
async def get_photo_id(message):
    print(message.photo[3].file_id)