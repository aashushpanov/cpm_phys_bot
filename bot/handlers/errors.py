from aiogram import Router
from aiogram.types.error_event import ErrorEvent
from aiogram.exceptions import (
    DetailedAiogramError
)

import logging



error_router = Router()

@error_router.error()
async def aiogram_error(event: ErrorEvent):
    logging.error(str(event))
