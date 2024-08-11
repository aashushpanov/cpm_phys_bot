from aiogram import F, types, Router
import datetime as dt

from data import config
from loader import bot
from utils.db.get import get_question


question_router = Router()

@question_router.message(F.chat.id==config.ADMIN_GROUP_ID)
async def question_answer(message: types.Message):
    if message.reply_to_message:
        bot_message = message.reply_to_message
        question = get_question(bot_message.message_id)
        answer = message.text
        text = 'Ответ на ваш вопрос:\n\n{}'.format(answer)
        await bot.send_message(
            question['user_id'],
            reply_to_message_id=question['user_message_id'],
            text=text
        )
        await message.reply(text=f'Ответ {answer} отправлен')
