import json

from .schema import ItemType

class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def is_configuration_json_valid(json_path: str) -> bool:
    """ Returns true if the given JSON file exists and is valid
    """
    try:
        with open(json_path, 'r') as file:
            json.load(file)
        return True
    except Exception:
        return False

def print_wizard_title(message: str) -> None:
    """ Prints the given message in the standard output using a bold and blue font
    """
    print(f'{TerminalColors.BOLD}{TerminalColors.OKBLUE}{message}{TerminalColors.ENDC}')
    print()

def print_wizard_message(message: str) -> None:
    """ Prints the given message in the standard output using a blue font
    """
    print(f'{TerminalColors.OKBLUE}{message}{TerminalColors.ENDC}')

def print_wizard_success(message: str) -> None:
    """ Prints the given message in the standard output using a green font
    """
    print()
    print(f'{TerminalColors.BOLD}{TerminalColors.OKGREEN}{message}{TerminalColors.ENDC}')

def get_wizard_input(message: str) -> str:
    try:
        value = input(f'- {TerminalColors.OKBLUE}{message}{TerminalColors.ENDC}: ')
    except Exception:
        return None
    return value

def print_wizard_warning(message: str) -> None:
    print(f"{TerminalColors.WARNING}[WARNING] {message}{TerminalColors.ENDC}")

def print_wizard_error(message: str) -> None:
    print(f"{TerminalColors.FAIL}[ERROR] {message}{TerminalColors.ENDC}")
