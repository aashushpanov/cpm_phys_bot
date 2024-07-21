from aiogram.filters import CallbackData

from bot.menu.logic.menu_classes import MenuNode


NO_IMPLEMENT_CALL = CallbackData('no_implement')


def set_user_menu(main_node=None):
    # main_menu
    #----------------------------------------------------------------
    user_menu = MenuNode()
    if main_node:
        main_node.set_child(user_menu)

    user_menu.set_childs([
        MenuNode('О нас'),
        MenuNode('Наши курсы', callback=NO_IMPLEMENT_CALL.new()),
        MenuNode('Зарегистрироваться', callback=NO_IMPLEMENT_CALL.new()),
        MenuNode('Подписаться'),
        MenuNode('Вопрос/Ответ'),
        MenuNode('Личный кабинет', callback=NO_IMPLEMENT_CALL.new()),
        MenuNode('FAQ', callback=NO_IMPLEMENT_CALL.new()),
        MenuNode('Наши соцсети', callback=NO_IMPLEMENT_CALL.new())
    ])

    user_menu.child(text='О нас').set_childs([
        MenuNode('Информация о нас', callback=NO_IMPLEMENT_CALL.new())
    ])

    user_menu.child(text='Подписаться на обновления').set_childs([
        MenuNode('Новости для 3-4 класса', callback=NO_IMPLEMENT_CALL.new()),
        MenuNode('Новости для 5-6 класса', callback=NO_IMPLEMENT_CALL.new()),
        MenuNode('Новости для 7-9 класса', callback=NO_IMPLEMENT_CALL.new()),
        MenuNode('Все новости', callback=NO_IMPLEMENT_CALL.new())
    ])

    user_menu.child(text='Вопрос/Ответ').set_childs([
        MenuNode('Задать вопрос', callback=NO_IMPLEMENT_CALL.new())
    ])