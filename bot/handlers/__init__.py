from aiogram import Router

from .errors import error_router
from .base import base_router
from .start import start_router
from .menus import menu_router


handlers_router = Router()

handlers_router.include_routers(
    error_router,
    base_router,
    start_router,
    menu_router
)
