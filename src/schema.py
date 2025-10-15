import json
from enum import Enum

class ItemType(Enum):
    STRING = 'string'
    NUMERIC = 'numeric'
    ARRAY = 'array'
    OBJECT = 'object'
    MAP = 'map'


class SchemaItem:
    pass


class SchemaItem:
    """ Class that parses the JSON and exposes its attributes
    """
    def __init__(self, item_dict: dict):
        self.__name = item_dict.get('name')
        self.__is_mandatory = item_dict.get('is_mandatory')
        self.__prompt = item_dict.get('prompt')

    @property
    def name(self) -> str:
        return self.__name

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
    def items(self) -> ItemType:
        return self.__items

    @property
    def items_number(self) -> int:
        return self.__items_number


class NumericSchemaItem(SchemaItem):
    def __init__(self, item_dict: dict):
        super().__init__(item_dict)


class StringSchemaItem(SchemaItem):
    def __init__(self, item_dict: dict):
        super().__init__(item_dict)


class ArraySchemaItem(SchemaItem):
    def __init__(self, item_dict: dict):
        super().__init__(item_dict)

        self.__items_number = None
        self.__items = SchemaItemFactory.get_schema_item(item_dict.get('items'))
        if items_number := item_dict.get('number_of_items'):
            if items_number <= 0:
                raise RuntimeError('Items number must have a positive '
                                    f'value, not \'{items_number}\'')
            self.__items_number = items_number

    @property
    def items(self) -> SchemaItem:
        return self.__items

    @property
    def items_number(self) -> int:
        return self.__items_number


class ObjectSchemaItem(SchemaItem):
    def __init__(self, item_dict: dict):
        super().__init__(item_dict)

        self.__fields = []
        for field_dict in item_dict.get('fields'):
            self.__fields.append(SchemaItemFactory.get_schema_item(field_dict))

    @property
    def fields(self) -> list:
        return self.__fields


class MapSchemaItem(SchemaItem):
    def __init__(self, item_dict: dict):
        super().__init__(item_dict)

        self.__items_number = None
        self.__items = SchemaItemFactory.get_schema_item(item_dict.get('items'))
        if items_number := item_dict.get('number_of_items'):
            if items_number <= 0:
                raise RuntimeError('Items number must have a positive '
                                    f'value, not \'{items_number}\'')
            self.__items_number = items_number

    @property
    def items(self) -> SchemaItem:
        return self.__items

    @property
    def items_number(self) -> int:
        return self.__items_number


class SchemaItemFactory:
    def get_schema_item(item_dict: dict):
        item_type = item_dict.get('type')
        if item_type == 'numeric':
            return NumericSchemaItem(item_dict)
        elif item_type == 'string':
            return StringSchemaItem(item_dict)
        elif item_type == 'array':
            return ArraySchemaItem(item_dict)
        elif item_type == 'object':
            return ObjectSchemaItem(item_dict)
        elif item_type == 'map':
            return MapSchemaItem(item_dict)
        else:
            raise RuntimeError(f'Type \'{item_type}\' is not a valid type')


class Schema:
    def __init__(self, json_path: dict):
        self.__json_path = json_path
        self.__root = None
        self.__load_schema()

    @property
    def json_path(self) -> dict:
        return self.__json_path

    @property
    def root(self) -> SchemaItem:
        return self.__root

    def __load_schema(self):
        """ Initialises the instance of the schema by loading the JSON file
        """
        with open(self.__json_path, 'r+') as file_reader:
            json_content = json.loads(file_reader.read())

        item_obj = SchemaItemFactory.get_schema_item(json_content)
        self.__root = item_obj
