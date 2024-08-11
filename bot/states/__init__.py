from aiogram import Router

from .user import user_state_router


state_router = Router()

state_router.include_routers(
    user_state_router
)
