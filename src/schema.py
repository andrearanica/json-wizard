import json
from enum import Enum

class ItemType(Enum):
    STRING = 'string'
    NUMERIC = 'numeric'
    ARRAY = 'array'
    OBJECT = 'object'

class SchemaItem:
    pass

class SchemaItem:
    """ Class that parses the JSON and exposes its attributes
    """
    def __init__(self, item_dict: dict):
        self.__name = item_dict.get('name')
        self.__type = ItemType(item_dict.get('type'))
        self.__is_mandatory = item_dict.get('is_mandatory')
        self.__prompt = item_dict.get('prompt')

        self.__fields = []
        if self.__type is ItemType.OBJECT:
            for field_dict in item_dict.get('fields'):
                self.__fields.append(SchemaItem(field_dict))

        self.__items = None
        if self.__type is ItemType.ARRAY:
            # FIXME iterate on items
            self.__items.append(SchemaItem(item_dict.get('items')))

        self.__number_of_items = None
        if self.__type is ItemType.ARRAY and item_dict.get('number'):
            self.__number_of_items = item_dict.get('number')

    @property
    def name(self) -> str:
        return self.__name

    @property
    def type(self) -> ItemType:
        return self.__type

    @property
    def is_mandatory(self) -> bool:
        return self.__is_mandatory

    @property
    def prompt(self) -> str:
        if self.__prompt:
            return self.__prompt
        else:
            return self.name

    @property
    def fields(self) -> list:
        return self.__fields

    @property
    def items(self) -> list:
        return self.__items

    @property
    def number_of_items(self) -> int:
        return self.__number_of_items

    def __repr__(self) -> str:
        obj_dict = {
            'name': self.__name,
            'type': self.__type,
            'is_mandatory': self.__is_mandatory,
            'prompt': self.__prompt
        }

        if self.__items:
            obj_dict.update({
                'items': self.__items
            })

        if self.__fields:
            obj_dict.update({
                'fields': self.__fields
            })

        return str(obj_dict)


class Schema:
    def __init__(self, json_path: dict):
        self.__json_path = json_path
        self.__items = []
        self.__load_schema()

    @property
    def json_path(self) -> dict:
        return self.__json_path

    @property
    def items(self) -> list[SchemaItem]:
        return self.__items

    def __load_schema(self):
        """ Initialises the instance of the schema by loading the JSON file
        """
        with open(self.__json_path, 'r+') as file_reader:
            json_content = json.loads(file_reader.read())

        if type(json_content) is dict:
            error = 'The configuration JSON must contain an array of elements, not a dict'
            raise RuntimeError(error)

        self.__items = []
        for item_dict in json_content:
            item_obj = SchemaItem(item_dict)
            self.__items.append(item_obj)
