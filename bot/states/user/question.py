from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StateGroup

from loader import bot
from data import config
from menu.by_user.user import HelpCallback
from utils.keyboards.common import cancel_keyboard


question_router = Router()


class AddQuestion(StateGroup):
    admin_question = State()


@question_router.callback_query(HelpCallback.filter(), F.action == 'q')
async def start(callback: types.CalbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer('Опишите проблему максимально точно и, при необходимости, укажите название '
                                  'олимпиады.\n\nНапишите вопрос здесь \U00002B07', reply_markup=cancel_keyboard())
    await state.set_state(AddQuestion.admin_question)


async def resieve_question(message: types.Message, state: FSMContext):
    question_text = message.test()
    text = f'вопрос {question_text}'
    await bot.send_message(chat_id=config.ADMIN_GROUP_ID, text=text)
    await state.clear()