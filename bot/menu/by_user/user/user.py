from aiogram.filters.callback_data import CallbackData

from menu.logic.menu_classes import InfoNode, MenuNode, NodeGenerator, NodeType
from .generators import show_events, event_options

from data.texts.about import text as about_text

class NoImplementCall(CallbackData, prefix='no_implement'):
    pass

class AboutCall(CallbackData, prefix='about'):
    pass


def set_user_menu(main_node=None):
    # main_menu
    #----------------------------------------------------------------
    user_menu = MenuNode(text='Меню')
    if main_node:
        main_node.set_child(user_menu)

    user_menu.set_childs([
        InfoNode('О нас', info=about_text),
        NodeGenerator('Наши курсы', func=show_events),
        MenuNode('Зарегистрироваться', callback=NoImplementCall().pack()),
        MenuNode('Подписаться на обновления'),
        MenuNode('Вопрос/Ответ'),
        MenuNode('Личный кабинет', callback=NoImplementCall().pack()),
        MenuNode('FAQ', callback=NoImplementCall().pack()),
        MenuNode('Наши соцсети')
    ])

    user_menu.child(text='Наши курсы').add_blind_node('event_list', type=NodeType.GENERATOR, func=event_options)
    user_menu.child(text='Наши курсы').blind_node.add_blind_node('event_opt')

    user_menu.child(text='Подписаться на обновления').set_childs([
        MenuNode('Новости для 3-4 класса', callback=NoImplementCall().pack()),
        MenuNode('Новости для 5-6 класса', callback=NoImplementCall().pack()),
        MenuNode('Новости для 7-9 класса', callback=NoImplementCall().pack()),
        MenuNode('Все новости', callback=NoImplementCall().pack())
    ])

    user_menu.child(text='Вопрос/Ответ').set_childs([
        MenuNode('Задать вопрос', callback=NoImplementCall().pack())
    ])

    user_menu.child(text='Наши соцсети').set_childs([
        MenuNode('ВКонтакте', callback='https://vk.com/physics_cpm'),
        MenuNode('Telegram', callback='https://t.me/physics_cpm')
    ])

    return user_menu
