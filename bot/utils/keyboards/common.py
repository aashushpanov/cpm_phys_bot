from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

import pandas as pd

from menu.logic.menu_classes import MenuNode, MoveCall
from utils.functions.functions import delete_message


class DeleteKeyboardCall(CallbackData, prefix='del'):
    pass

class CancelEventCall(CallbackData, prefix='cancel_event'):
    pass
class PageKeyboardMoveCall(CallbackData, prefix='page_move'):
    data: str

class PageKeyboardCall(CallbackData, prefix='pk'):
    data: str


async def delete_keyboard(callback: CallbackQuery, state: FSMContext = None):
    if state:
        await state.finish()
    await delete_message(callback.message)


async def tree_menu_keyboard(menu_node: MenuNode, callback: MoveCall = None, data=None):
    if callback is not None:
        row_width = callback.width
    else:
        row_width = 1
    markup = InlineKeyboardBuilder()

    async for _, text, node_callback in menu_node.childs_data(callback=callback, data=data):
        if node_callback.__contains__('://'):
            markup.row(InlineKeyboardButton(text=text, url=node_callback))
        else:
            markup.row(InlineKeyboardButton(text=text, callback_data=node_callback))

    if menu_node.parent:
        markup.add(
            InlineKeyboardButton(text="\U00002B05 Назад",
                                 callback_data=MoveCall(action='u', node=menu_node.id, data='', width=1).pack()))
    markup.adjust(row_width)
    return markup.as_markup()
        

def yes_no_keyboard(callback):
    markup = InlineKeyboardBuilder()

    markup.add(InlineKeyboardButton(text='\U00002705 Да', callback_data=callback))
    markup.add(InlineKeyboardButton(text='\U0000274C Нет', callback_data=DeleteKeyboardCall().pack()))

    return markup.as_markup()


def cancel_keyboard():
    markup = InlineKeyboardBuilder()
    markup.add(InlineKeyboardButton(text='\U0000274C Отмена', callback_data=CancelEventCall().pack()))
    return markup.as_markup()


def callbacks_keyboard(texts: list, callbacks: list, cancel_button: bool = False):
    if len(texts) != len(callbacks) and len(callbacks) != 0:
        raise KeyError
    button_dict = dict(zip(texts, callbacks))
    markup = InlineKeyboardBuilder()
    for text, callback in button_dict.items():
        if isinstance(callback, str) and isinstance(text, str):
            if callback.__contains__('://'):
                markup.add(InlineKeyboardButton(text=text, url=callback))
            else:
                markup.add(InlineKeyboardButton(text=text, callback_data=callback))
        else:
            raise TypeError
    if cancel_button:
        markup.add(InlineKeyboardButton(text='\U0000274C Отмена', callback_data=CancelEventCall().pack()))
    return markup.as_markup()


def pages_keyboard(list_of_instance: pd.DataFrame, callback_column: str, text_column: str, page: int, height: int = 5):
    """
    Он принимает фрейм данных, столбец для использования в качестве данных обратного вызова, столбец для использования в
    качестве текста, текущую страницу и количество строк на странице и возвращает клавиатуру со строками фрейма данных в
    качестве кнопок.

    :param list_of_instance: pd.DataFrame — кадр данных, содержащий данные, которые вы хотите отобразить
    :type list_of_instance: pd.DataFrame
    :param callback_column: столбец в кадре данных, который содержит данные обратного вызова
    :type callback_column: str
    :param text_column: столбец в кадре данных, содержащий текст, который будет отображаться на кнопке
    :type text_column: str
    :param page: int - номер страницы
    :type page: int
    :param height: количество строк для отображения на странице, defaults to 5
    :type height: int (optional)
    :return: Объект InlineKeyboardMarkup
    """
    if list_of_instance.shape[0] - (page + 1) * height == 1:
        top = (page + 1) * height + 1
        last_page = True
    else:
        top = (page + 1) * height
        last_page = False
    if list_of_instance.shape[0] < (page + 1) * height:
        last_page = True
    page_list = list_of_instance.iloc[height*page:top]
    markup = InlineKeyboardBuilder()
    for _, row in page_list.iterrows():
        markup.add(InlineKeyboardButton(text=row[text_column],
                                           callback_data=PageKeyboardCall().new(data=row[callback_column])), width=1)
    left_btn = None
    right_btn = None
    if page != 0:
        left_btn = InlineKeyboardButton(text='\U000025C0', callback_data=PageKeyboardMoveCall(data='decr').pack())
    if not last_page:
        right_btn = InlineKeyboardButton(text='\U000025B6', callback_data=PageKeyboardMoveCall(data='incr').pack())
    if right_btn is None and left_btn is None:
        return markup.as_markup()
    elif right_btn and left_btn:
        markup.row(left_btn, right_btn)
    else:
        if left_btn:
            btn = left_btn
        else:
            btn = right_btn
        markup.row(btn)
    return markup.as_markup()