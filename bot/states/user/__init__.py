from aiogram import Router

from .question import question_router


user_state_router = Router(
    question_router
)
