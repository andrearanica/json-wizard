import os
import sys

from src.schema import Schema
from src.wizard import Wizard
from src.utils import *

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_wizard_error('Please provide the path to the configuration JSON '
                           'file as the first argument.')
        sys.exit(1)

    configuration_json_path = sys.argv[1]
    if not os.path.exists(configuration_json_path):
        print_wizard_error('The configuration JSON file at '
                           f'\'{configuration_json_path}\' does not exist.')
        sys.exit(1)

    if not is_configuration_json_valid(configuration_json_path):
        print_wizard_error('The configuration JSON file at '
                           f'\'{configuration_json_path}\' is not valid.')
        sys.exit(1)

    if len(sys.argv) >= 3:
        destination_json_path = sys.argv[2]
    else:
        print_wizard_warning('Destination JSON path not provided; using the '
                             'default one (\'result.json\' in the current '
                             'directory).')
        destination_json_path = os.path.join(os.getcwd(), 'result.json')

    schema = Schema(json_path=configuration_json_path)
    wizard = Wizard(schema)
    wizard.start()
    with open(destination_json_path, 'w+') as file_writer:
        file_writer.write(json.dumps(wizard.result))
