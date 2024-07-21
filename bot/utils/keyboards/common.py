from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

from bot.menu.logic.menu_classes import MenuNode, MOVE_CALL
from utils.functions.functions import delete_message


DELETE_KEYBOARD_CALL = CallbackData('del')
CANCEL_EVENT_CALL = CallbackData('cancel_event')
PAGE_KEYBOARD_MOVE_CALL = CallbackData('page_move', 'data')
PAGE_KEYBOARD_CALL = CallbackData('pk', 'data')


async def delete_keyboard(callback: CallbackQuery, state: FSMContext = None):
    if state:
        await state.finish()
    await delete_message(callback.message)


async def tree_menu_keyboard(menu_node: MenuNode, callback: CallbackQuery = None, data=None):
    if callback is not None:
        row_width = int(callback.data.split(':')[-1])
    else:
        row_width = 1
    markup = InlineKeyboardMarkup(row_width=row_width)

    async for _, text, node_callback in menu_node.childs_data(callback=callback, data=data):
        if node_callback.__contains__('://'):
            markup.insert(InlineKeyboardButton(text=text, url=node_callback))
        else:
            markup.insert(InlineKeyboardButton(text=text, callback_data=node_callback))

    if menu_node.parent:
        markup.insert(
            InlineKeyboardButton(text="\U00002B05 Назад",
                                 callback_data=MOVE_CALL.new(action='u', node=menu_node.id, data='', width=1)))
        

def yes_no_keyboard(callback):
    markup = InlineKeyboardMarkup()

    markup.insert(InlineKeyboardButton(text='\U00002705 Да', callback_data=callback))
    markup.insert(InlineKeyboardButton(text='\U0000274C	Нет', callback_data=DELETE_KEYBOARD_CALL.new()))

    return markup


def cansel_keyboard():
    markup = InlineKeyboardMarkup()
    markup.insert(InlineKeyboardButton(text='\U0000274C Отмена', callback_data=CANCEL_EVENT_CALL.new()))
    return markup


def callbacks_keyboard(texts: list, callbacks: list, cansel_button: bool = False):
    if len(texts) != len(callbacks) and len(callbacks) != 0:
        raise KeyError
    button_dict = dict(zip(texts, callbacks))
    markup = InlineKeyboardMarkup(row_width=1)
    for text, callback in button_dict.items():
        if isinstance(callback, str) and isinstance(text, str):
            if callback.__contains__('://'):
                markup.insert(InlineKeyboardButton(text=text, url=callback))
            else:
                markup.insert(InlineKeyboardButton(text=text, callback_data=callback))
        else:
            raise TypeError
    if cansel_button:
        markup.insert(InlineKeyboardButton(text='\U0000274C Отмена', callback_data=CANCEL_EVENT_CALL.new()))
    return markup


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
    markup = InlineKeyboardMarkup(row_width=1)
    for _, row in page_list.iterrows():
        markup.insert(InlineKeyboardButton(text=row[text_column],
                                           callback_data=PAGE_KEYBOARD_CALL.new(data=row[callback_column])))
    left_btn = None
    right_btn = None
    if page != 0:
        left_btn = InlineKeyboardButton(text='\U000025C0', callback_data=PAGE_KEYBOARD_MOVE_CALL.new(data='decr'))
    if not last_page:
        right_btn = InlineKeyboardButton(text='\U000025B6', callback_data=PAGE_KEYBOARD_MOVE_CALL.new(data='incr'))
    if right_btn is None and left_btn is None:
        return markup
    elif right_btn and left_btn:
        markup.row(left_btn, right_btn)
    else:
        if left_btn:
            btn = left_btn
        else:
            btn = right_btn
        markup.row(btn)
    return markup