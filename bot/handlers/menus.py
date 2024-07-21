from aiogram import Router
from aiogram import types
from aiogram.filters import Command

from menu.logic.structure import user_menu, list_menu


menu_router = Router()

def get_access():
    return 1

@menu_router.message(Command['menu'])
async def show_main_menu(message: types.Message, state=None):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer('Действие отменено')
    match get_access(user_id=message.from_user.id):
        case _:
            menu = user_menu
    await list_menu(message, menu=menu, title='Меню')
