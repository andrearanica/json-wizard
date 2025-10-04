import os
from .schema import Schema, SchemaItem, ItemType
from .utils import *

class Wizard:
    def __init__(self, schema: Schema):
        self.__schema = schema
        self.__result = {}

    @property
    def schema(self) -> Schema:
        return self.__schema

    @property
    def result(self):
        return self.__result

    def start(self):
        """ Starts the Wizard process
        """
        if self.__result != {}:
            raise RuntimeError(f"The wizard has already been executed!")

        print_wizard_title(f'{TerminalColors.BOLD}{TerminalColors.OKBLUE}**** Welcome to the JSON Wizard! 🪄 ​****{TerminalColors.ENDC}')

        self.__result = self.__execute_wizard(self.schema.root)

        print_wizard_success(f'The JSON file has been succesfully created!')
    
    def __execute_wizard(self, item: SchemaItem):
        """ Asks the user to compile the given item
        """
        if item.type in [ItemType.STRING, ItemType.NUMERIC]:
            item_value = get_wizard_input(item.prompt)

            if not item_value and not item.is_mandatory:
                return

            while not item_value and item.is_mandatory:
                if item.type is ItemType.NUMERIC:
                    if item_value.isnumeric():
                        item_value = float(item_value)
                else:
                    item_value = get_wizard_input(item.prompt)

            return item_value

        elif item.type is ItemType.OBJECT:
            obj = {}
            for field in item.fields:
                field_value = self.__execute_wizard(field)
                if field_value is not None:
                    obj[field.name] = field_value
            return obj

        elif item.type is ItemType.ARRAY:
            array = []
            wants_to_continue = True
            while wants_to_continue:
                new_item = self.__execute_wizard(item.items)
                if new_item is not None:
                    array.append(new_item)

                wants_to_continue_raw = get_wizard_input(f'Add another item for \'{item.name}\'? (Y/N)')
                wants_to_continue = wants_to_continue_raw.upper() == 'Y'
            return array
