from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from loader import bot
from data import config
from menu.by_user.user.user import HelpCallback
from utils.keyboards.common import cancel_keyboard
from utils.db.add import add_question


question_router = Router()


class AddQuestion(StatesGroup):
    admin_question = State()


@question_router.callback_query(HelpCallback.filter())
async def start(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Опишите проблему максимально точно и, при необходимости, укажите название '
                                  'курса.\n\nНапишите вопрос здесь \U00002B07', reply_markup=cancel_keyboard())
    await state.set_state(AddQuestion.admin_question)


@question_router.message(AddQuestion.admin_question, F.text)
async def receive_question(message: types.Message, state: FSMContext):
    question_text = message.text
    user_message_id = message.message_id
    user_id = message.from_user.id
    bot_message = await bot.forward_message(chat_id=config.ADMIN_GROUP_ID, from_chat_id=message.chat.id, message_id=message.message_id)
    bot_message_id = bot_message.message_id
    status = add_question(user_id, user_message_id, bot_message_id, question_text, message.date.timestamp())
    if status:
        await message.answer("Ваш вопрос отправлен")
    else:
        await message.answer("Что-то пошло не так")
    await state.clear()
