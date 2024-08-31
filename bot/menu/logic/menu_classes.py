import enum

from aiogram import types
from aiogram.filters.callback_data import CallbackData


class NodeType(enum.Enum):
    SIMPLE = 1
    GENERATOR = 2


class MoveCall(CallbackData, prefix='move'):
    action: str
    node: str
    data: str
    width: int


class BaseNode:
    def __init__(self, _id: str, text, parent, callback, photo_id, info):
        self._id = _id
        self._childs = []
        self._text = text
        self._parent = parent
        self._callback = callback
        self._photo_id = photo_id
        self._info = info
        if photo_id:
            self._photo = types.input_media_photo.InputMediaPhoto(media=photo_id, caption=self._info)
        else:
            self._photo = None

    def childs(self):
        result = {}
        for child in self._childs:
            result.update({child.id: child})
        return result

    def all_childs(self, result=None):
        if result is None:
            result = {}
        childs = self.childs()
        result.update(childs)
        for child in self._childs:
            result = child.all_childs(result)
        return result

    @staticmethod
    def have_childs():
        return True

    @property
    def id(self):
        return self._id if self._id else 0
    
    @property
    def info(self):
        return self._info
    
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def parent(self):
        return self._parent

    @property
    def callback(self):
        return self._callback

    @property
    def photo_id(self):
        return self._photo_id
    
    @property
    def photo(self):
        return self._photo


class InfoNode(BaseNode):
    def __init__(self, text, info, callback=None, parent=None, _id=None, photo_id=None):
        super().__init__(_id=_id or 'admin', parent=parent, callback=callback, photo_id=photo_id, text=text, info=info)
    
    @staticmethod
    def have_childs():
        return False


class MenuNode(BaseNode):
    def __init__(self, text: str = None, info=None, photo_id=None, callback=None, parent=None, _id=None, row_width=1):
        super().__init__(_id=_id or 'admin', parent=parent, callback=callback, photo_id=photo_id, text=text, info=info)
        self._row_width = row_width

    async def childs_data(self, **kwargs):
        for child in self._childs:
            yield child.id, child.text, child.callback

    def child(self, child_id: str = None, text: str = None):
        if child_id is not None:
            for child in self._childs:
                if child.id == child_id:
                    return child
        elif text:
            for child in self._childs:
                if child.text == text:
                    return child
        raise KeyError

    def set_child(self, child):
        child._id = self._id + '_' + str(len(self._childs))
        if child.callback is None:
            match child:
                case InfoNode():
                    child._callback = MoveCall(action='i', node=child.id, data='', width=1).pack()
                case _:
                    child._callback = MoveCall(action='d', node=child.id, data='', width=1).pack()
        self._childs.append(child)
        child._parent = self

    def set_childs(self, childs):
        for child in childs:
            self.set_child(child)

    def prev(self):
        return self._parent

    def clean_childs(self):
        if self._childs:
            for child in self._childs:
                child.clean_childs()
                self._childs.clear()
        else:
            self._parent = None


class NodeGenerator(MenuNode):
    def __init__(self, text, func, info=None, photo_id=None, _id=None, reg_nodes=None, parent=None, callback=None):
        super().__init__(_id=_id if id else 'gen', parent=parent, callback=callback, info=info, text=text, photo_id=photo_id)
        if reg_nodes is None:
            reg_nodes = []
        self._func = func
        self._reg_nodes = reg_nodes
        self._sub_childs = []
        self._blind_node = None

    @property
    def func(self):
        return self._func

    async def childs_data(self, **kwargs):
        for child in self._reg_nodes:
            yield child.id, child.text, child.callback
        async for child in self.func(self, **kwargs):
            yield child.id, child.text, child.callback

    def append(self, node):
        self._reg_nodes.append(node)

    def add_blind_node(self, node_id, type: NodeType=NodeType.SIMPLE, func=None, row_width=1, text=None):
        node_id = self.id + '_' + node_id
        if type == NodeType.SIMPLE:
            self._blind_node = BlindNode(node_id, self, row_width=row_width)
        if type == NodeType.GENERATOR:
            if text is None:
                text = 'Меню'
            self._blind_node = NodeGenerator(text=text, func=func, _id=node_id)
        self._blind_node._parent = self

    def set_sub_child(self, sub_child):
        sub_child._id = self.blind_node.id + '_' + str(len(self.blind_node._childs))
        self._blind_node._childs.append(sub_child)
        sub_child._parent = self.blind_node

    def set_sub_childs(self, sub_childs):
        for sub_child in sub_childs:
            self.set_sub_child(sub_child)

    @property
    def blind_node(self):
        return self._blind_node

    def childs(self):
        result = {}
        for child in self._childs:
            result.update({child.id: child})
        result.update({self.blind_node.id: self.blind_node})
        result.update(self.blind_node.childs())
        return result


class BlindNode(MenuNode):
    def __init__(self, node_id, parent, row_width=1):
        super().__init__(_id=node_id, parent=parent, callback=None, row_width=row_width)

    def childs(self):
        result = {}
        for child in self._childs:
            result.update({child.id: child})
        return result
