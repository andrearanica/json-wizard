from .schema import *
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

        print_wizard_title(f'**** Welcome to the JSON Wizard! 🪄  ​****')

        self.__result = self.__execute_wizard(self.schema.root)

        print_wizard_success(f'The JSON file has been succesfully created!')
    
    def __execute_wizard(self, item: SchemaItem):
        """ Asks the user to compile the given item
        """
        if isinstance(item, StringSchemaItem) or isinstance(item, NumericSchemaItem):
            while True:
                item_value = get_wizard_input(item.prompt)

                if not item_value and not item.is_mandatory:
                    break

                if isinstance(item, NumericSchemaItem):
                    if item_value.isnumeric():
                        item_value = float(item_value)
                    else:
                        print_wizard_warning(f'\'{item_value}\' is not valid '
                                              ' for a numeric field')
                        item_value = None

                if item_value:
                    break

                print_wizard_warning(f'This field is mandatory: please insert '
                                      ' a value')

            return item_value

        elif isinstance(item, ObjectSchemaItem):
            obj = {}
            for field in item.fields:
                field_value = self.__execute_wizard(field)
                if field_value is not None:
                    obj[field.name] = field_value
            return obj

        elif isinstance(item, ArraySchemaItem):
            array = []
            wants_to_continue = True
            while wants_to_continue:
                new_item = None
                new_item = self.__execute_wizard(item.items)
                if new_item is not None:
                    array.append(new_item)

                wants_to_continue_raw = get_wizard_input('Add another item '
                                                         f'for \'{item.name}\'?'
                                                         ' (Y/n)')
                wants_to_continue = not wants_to_continue_raw.upper() == 'N'
            return array

        elif isinstance(item, MapSchemaItem):
            map_obj = {}
            i = 1
            wants_to_continue = True
            while wants_to_continue:
                item_key = get_wizard_input(item.prompt)
                if map_obj.get(item_key) is not None:
                    print_wizard_warning(f'The key \'{item_key}\' has '
                                            'already been used; it will be '
                                            'overwritten with the new value '
                                            'you will insert now.')
                if not item_key:
                    print_wizard_warning(f'Please insert a valid key')
                    continue

                map_obj[item_key] = self.__execute_wizard(item.items)

                if item.items_number is not None:
                    wants_to_continue = i < item.items_number
                    i += 1
                else:
                    wants_to_continue = get_wizard_input('Add another item for '
                                                         f'\'{item.name}\'? '
                                                         '(Y/n)').upper() != 'N'
            return map_obj
