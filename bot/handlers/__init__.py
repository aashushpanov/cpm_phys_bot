from aiogram import Router

from .errors import error_router
from .cancel import cancel_router
from .base import base_router
from .texts import start_router
from .menus import menu_router
from .by_user import users_handlers_router


handlers_router = Router()

handlers_router.include_routers(
    error_router,
    cancel_router,
    base_router,
    start_router,
    menu_router,
    users_handlers_router
)
