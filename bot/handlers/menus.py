from aiogram import Router
from aiogram import types
from aiogram.filters import Command

import aiogram.filters.callback_data
from menu.logic.structure import main_menu, list_menu
from menu.logic.menu_classes import MoveCall


menu_router = Router()

def get_access(user_id):
    return 1

@menu_router.message(Command('menu'))
async def show_main_menu(message: types.Message, state=None):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer('Действие отменено')
    match get_access(user_id=message.from_user.id):
        case _:
            menu = main_menu
    await list_menu(message, menu=menu, title='Меню')


@menu_router.callback_query(MoveCall.filter())
async def change_menu(callback: types.CallbackQuery, callback_data: MoveCall):
    await list_menu(callback, callback_data)

