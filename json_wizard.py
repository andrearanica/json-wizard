import os
import sys

from src.schema import Schema
from src.wizard import Wizard
from src.utils import *

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"{TerminalColors.FAIL}[ERROR] Please provide the path to the configuration JSON file as the first argument.{TerminalColors.ENDC}")
        sys.exit(1)

    configuration_json_path = sys.argv[1]
    if not os.path.exists(configuration_json_path):
        print(f"{TerminalColors.FAIL}[ERROR] The configuration JSON file at '{configuration_json_path}' does not exist.{TerminalColors.ENDC}")
        sys.exit(1)

    if not is_configuration_json_valid(configuration_json_path):
        print(f"{TerminalColors.FAIL}[ERROR] The configuration JSON file at '{configuration_json_path}' is not valid.{TerminalColors.ENDC}")
        sys.exit(1)

    if len(sys.argv) >= 3:
        destination_json_path = sys.argv[2]
    else:
        print(f"{TerminalColors.WARNING}[WARNING] Destination JSON path not provided; using the default one ('result.json' in the current directory).{TerminalColors.ENDC}")
        destination_json_path = os.path.join(os.getcwd(), 'result.json')

    schema = Schema(json_path=configuration_json_path)
    wizard = Wizard(schema)
    wizard.start()
    with open(destination_json_path, 'w+') as file_writer:
        file_writer.write(json.dumps(wizard.result))
