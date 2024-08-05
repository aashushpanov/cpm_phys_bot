import pandas as pd

from utils.db.get import get_events, get_event
from menu.logic.menu_classes import MenuNode, MoveCall


async def show_events(node, **kwargs):
    callback = kwargs.pop('callback')
    events = get_events()
    if events.empty:
        await callback.answer('Событий нет', show_alert=True)
    for _, event in events.iterrows():
        name = event['name']
        _id = str(event.id)
        yield MenuNode(text=name, callback=MoveCall(action='d', node=node.blind_node.id, data=_id, width=1).pack())



async def event_options(node, **kwargs):
    callback = kwargs.pop('callback')
    event_id = callback.data
    event = get_event(event_id)
    text = event.description
    reg_url = event.reg_url
    node.text=text
    if reg_url:
        yield MenuNode(text="Основная информация", callback=reg_url)