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

        for item in self.schema.items:
            self.__wizard_on_item(item, self.__result)

        print_wizard_success(f'The JSON file has been succesfully created!')
    
    def __wizard_on_item(self, item: SchemaItem, result: dict):
        """ Asks the user to compile the given item
        """
        if item.type in [ItemType.STRING, ItemType.NUMERIC]:
            item_value = get_wizard_input(item.prompt)

            if not item_value and not item.is_mandatory:
                return

            while not item_value and item.is_mandatory:
                item_value = get_wizard_input(item.prompt)

            if item.type is ItemType.NUMERIC:
                if not item_value.isnumeric():
                    raise RuntimeError(f'\'{item.name}\' is a numeric item, but \'{item_value}\' cannot be converted to a numeric value')
                item_value = float(item_value)
            
            if isinstance(result, dict):
                result[item.name] = item_value
            elif isinstance(result, list):
                result.append(item_value)
        elif item.type is ItemType.OBJECT:
            result[item.name] = {}
            for field in item.fields:
                self.__wizard_on_item(field, result[item.name])
        elif item.type is ItemType.ARRAY:
            result[item.name] = []
            i = 0
            wants_to_continue = True
            while wants_to_continue:
                self.__wizard_on_item(item.items, result[item.name])
                i += 1

                wants_to_continue_raw = get_wizard_input(f'Add another item for \'{item.name}\'? (Y/N)')
                wants_to_continue = wants_to_continue_raw.upper() == 'Y'
