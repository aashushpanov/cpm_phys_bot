from aiogram import types

from utils.keyboards.common import tree_menu_keyboard
from menu.by_user.user.user import set_user_menu


main_menu = set_user_menu()
menu_childs = main_menu.all_childs()


async def list_menu(callback: types.CallbackQuery | types.Message, callback_data: dict = None, menu=None, title=''):
    match callback:
        case types.Message():
            markup = await tree_menu_keyboard(menu)
            await callback.answer(title, reply_markup=markup, parse_mode="MarkdownV2")
        case types.CallbackQuery():
            await callback.answer()
            if callback_data.action == "d":
                next_node = menu_childs.get(callback_data.node)
            elif callback_data.action == 'u':
                next_node = menu_childs.get(callback_data.node).parent
            elif callback_data.action == 'i':
                next_node = menu_childs.get(callback_data.node)
            else:
                raise KeyError
            markup = await tree_menu_keyboard(next_node, callback_data)
            if next_node.info:
                text = next_node.info
            else:
                text = next_node.text
            text = text.replace('.', '\.').replace('(', '\(').replace(')', '\)')
            await callback.message.edit_text(text=text, reply_markup=markup, parse_mode="MarkdownV2")
