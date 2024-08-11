from aiogram import Router

from .admin import admin_handlers_router


users_handlers_router = Router()


users_handlers_router.include_routers(
    admin_handlers_router
)
