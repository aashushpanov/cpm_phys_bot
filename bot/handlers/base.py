from aiogram.types.callback_query import CallbackQuery
from aiogram import Router, F


base_router = Router()

@base_router.callback_query(F.data == 'no_implement')
async def no_implemented(callback: CallbackQuery):
    await callback.answer('Появится позже', show_alert=True)
