from aiogram.filters.callback_data import CallbackData

from menu.logic.menu_classes import InfoNode, MenuNode, NodeGenerator, NodeType
from .generators import show_events, event_options, show_reg_urls

from data.texts.about import text as about_text
import data.texts.faq as faq


class NoImplementCall(CallbackData, prefix='no_implement'):
    pass


class HelpCallback(CallbackData, prefix='help'):
    type: str


def set_user_menu(main_node=None):
    # main_menu
    #----------------------------------------------------------------
    user_menu = MenuNode(text='Меню', photo_id='AgACAgIAAxkBAAIBxGbTbx7kcsC-aK36sykeXXRmnm45AAK14zEbiRmhSjcqeCctM1q7AQADAgADeAADNQQ')
    if main_node:
        main_node.set_child(user_menu)

    user_menu.set_childs([
        InfoNode('О нас', info=about_text, photo_id='AgACAgIAAxkBAAIBuWbB5_SsWa0_Ncv1oefsFbuAgiOJAAKr3DEbN5gQSgkfg76cuRqWAQADAgADeAADNQQ'),

        NodeGenerator('Наши курсы', func=show_events, info='Предлагаем Вам ознакомиться с нашими актуальными курсами👇',
                      photo_id='AgACAgIAAxkBAAIBumbB6AM8Ajlxty4hR_aDpHgfqwrwAAKs3DEbN5gQSl9QsEHoRfA9AQADAgADeAADNQQ'),

        NodeGenerator('Зарегистрироваться на курсы', func=show_reg_urls, info='Выберите курс, который Вас заинтересовал. По ссылке Вы сможете пройти записаться на него.',
                      photo_id='AgACAgIAAxkBAAIBnWbB1q6nexBiUacRPYGkamS_TekwAAIx3DEbN5gQSqx-eC7CfjPRAQADAgADeAADNQQ'),

        # MenuNode('Подписаться на обновления', info='Подпишитесь на обновления и получайте первыми актуальную информацию о новостях проекта и курсах, анонсы новых мероприятий и бесплатные материалы. мероприятия',
        #          photo_id='AgACAgIAAxkBAAIBu2bB6BGR_pBJWWZ8uxEXMUwfPVK0AAKt3DEbN5gQStM1DUJpYCb9AQADAgADeAADNQ'),
        # MenuNode('Личный кабинет', callback=NoImplementCall().pack()),
        MenuNode('FAQ', photo_id='AgACAgIAAxkBAAIBxWbTb0hN8IA7WQ6hxTfYQs_5X6dbAAK34zEbiRmhSmrwOO2N0OEJAQADAgADeAADNQQ'),
        MenuNode('Наши соцсети', photo_id='AgACAgIAAxkBAAIBxmbTb1knDClbd49qp1mLze30AziyAAK44zEbiRmhSsqUZ58YdWh8AQADAgADeAADNQQ'),
    ])

    user_menu.child(text='Наши курсы').add_blind_node('event_list', type=NodeType.GENERATOR, func=event_options)
    user_menu.child(text='Наши курсы').blind_node.add_blind_node('event_opt')

    user_menu.child(text='Зарегистрироваться на курсы').add_blind_node('event_reg')

    # user_menu.child(text='Подписаться на обновления').set_childs([
    #     MenuNode('Новости для 3-4 класса', callback=NoImplementCall().pack()),
    #     MenuNode('Новости для 5-6 класса', callback=NoImplementCall().pack()),
    #     MenuNode('Новости для 7-9 класса', callback=NoImplementCall().pack()),
    #     MenuNode('Все новости', callback=NoImplementCall().pack())
    # ])

    user_menu.child(text='FAQ').set_childs([
        InfoNode('Кто преподаватели? ', photo_id='AgACAgIAAxkBAAIBxWbTb0hN8IA7WQ6hxTfYQs_5X6dbAAK34zEbiRmhSmrwOO2N0OEJAQADAgADeAADNQQ', info=faq.preps),
        InfoNode('Есть ли занятия онлайн?', photo_id='AgACAgIAAxkBAAIBxWbTb0hN8IA7WQ6hxTfYQs_5X6dbAAK34zEbiRmhSmrwOO2N0OEJAQADAgADeAADNQQ', info=faq.online),
        InfoNode('Где найти годовую программу?', photo_id='AgACAgIAAxkBAAIBxWbTb0hN8IA7WQ6hxTfYQs_5X6dbAAK34zEbiRmhSmrwOO2N0OEJAQADAgADeAADNQQ', info=faq.year_pr),
        InfoNode('Где проходят занятия?', photo_id='AgACAgIAAxkBAAIBxWbTb0hN8IA7WQ6hxTfYQs_5X6dbAAK34zEbiRmhSmrwOO2N0OEJAQADAgADeAADNQQ', info=faq.addr),
        InfoNode('В чем преимущество «Физики ЦПМ»?', photo_id='AgACAgIAAxkBAAIBxWbTb0hN8IA7WQ6hxTfYQs_5X6dbAAK34zEbiRmhSmrwOO2N0OEJAQADAgADeAADNQQ', info=faq.cpm),
        InfoNode('Что такое «Физика ЦПМ»?', photo_id='AgACAgIAAxkBAAIBxWbTb0hN8IA7WQ6hxTfYQs_5X6dbAAK34zEbiRmhSmrwOO2N0OEJAQADAgADeAADNQQ', info=faq.about),
        InfoNode('Сколько стоят курсы?', photo_id='AgACAgIAAxkBAAIBxWbTb0hN8IA7WQ6hxTfYQs_5X6dbAAK34zEbiRmhSmrwOO2N0OEJAQADAgADeAADNQQ', info=faq.price),
        MenuNode('Задать вопрос', callback=HelpCallback(type='q').pack())
    ])

    user_menu.child(text='Наши соцсети').set_childs([
        MenuNode('ВКонтакте', callback='https://vk.com/physics_cpm'),
        MenuNode('Telegram', callback='https://t.me/physics_cpm')
    ])

    return user_menu
