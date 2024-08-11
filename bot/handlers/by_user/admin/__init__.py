from aiogram import Router

from .question_answer import question_router


admin_handlers_router = Router()

admin_handlers_router.include_routers(
    question_router
)