from aiogram.filters.callback_data import CallbackData

from menu.logic.menu_classes import MenuNode


class NoImplementCall(CallbackData, prefix='no_implement'):
    pass


def set_user_menu(main_node=None):
    # main_menu
    #----------------------------------------------------------------
    user_menu = MenuNode(text='Меню')
    if main_node:
        main_node.set_child(user_menu)

    user_menu.set_childs([
        MenuNode('О нас'),
        MenuNode('Наши курсы', callback=NoImplementCall().pack()),
        MenuNode('Зарегистрироваться', callback=NoImplementCall().pack()),
        MenuNode('Подписаться на обновления'),
        MenuNode('Вопрос/Ответ'),
        MenuNode('Личный кабинет', callback=NoImplementCall().pack()),
        MenuNode('FAQ', callback=NoImplementCall().pack()),
        MenuNode('Наши соцсети', callback=NoImplementCall().pack())
    ])

    user_menu.child(text='О нас').set_childs([
        MenuNode('Информация о нас', callback=NoImplementCall().pack())
    ])

    user_menu.child(text='Подписаться на обновления').set_childs([
        MenuNode('Новости для 3-4 класса', callback=NoImplementCall().pack()),
        MenuNode('Новости для 5-6 класса', callback=NoImplementCall().pack()),
        MenuNode('Новости для 7-9 класса', callback=NoImplementCall().pack()),
        MenuNode('Все новости', callback=NoImplementCall().pack())
    ])

    user_menu.child(text='Вопрос/Ответ').set_childs([
        MenuNode('Задать вопрос', callback=NoImplementCall().pack())
    ])

    return user_menu
