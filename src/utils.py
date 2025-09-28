import json

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
