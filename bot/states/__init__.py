from aiogram import Router

from .user import user_state_router


state_router = Router(
    user_state_router
)
