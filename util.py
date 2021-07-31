from colorama import init, Fore, Back, Style
init()
from sys import stdout # Needed for weird colorama hack on windows

def print_warning(msg: str):
    print(f"{Style.BRIGHT}{Fore.YELLOW}{msg}{Style.RESET_ALL}")

def print_success(msg: str):
    print(f"{Fore.GREEN}{Style.BRIGHT}{msg}{Style.RESET_ALL}")

def print_bold(msg: str):
    print(f"{Style.BRIGHT}{msg}{Style.RESET_ALL}")


def fuzzy_match_name(actual_name: str, other_name_start: str):
        if actual_name is None or other_name_start is None:
            return False
        if len(actual_name) == 0 or len(other_name_start) == 0:
            return False
        name_lower = actual_name.casefold().replace(" ", "")
        other_lower_start = other_name_start.casefold().replace(" ", "")
        return name_lower.startswith(other_lower_start)

def fuzzy_find_by_name(d: dict, full_name: str):
    for entry in d.items():
        possible_name_start = entry[0]
        if fuzzy_match_name(full_name, possible_name_start):
            # print(f"Found match for {full_name}: {entry}")
            return entry[1]
    return None