from aiogram import Router

from .question import question_router


user_state_router = Router()

user_state_router.include_routers(
    question_router
)
