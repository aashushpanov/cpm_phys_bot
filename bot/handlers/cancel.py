from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command


from utils.functions.functions import delete_message
from utils.keyboards.common import CancelEventCall


cancel_router = Router()

@cancel_router.callback_query(CancelEventCall.filter())
@cancel_router.message(Command('cancel'))
async def cancel(message: types.Message | types.CallbackQuery, state: FSMContext):
    await state.clear()
    if type(message) == types.CallbackQuery:
            await message.answer()
            message = message.message
    await message.answer('Действие отменено')
    await delete_message(message)
