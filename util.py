from bcolors import bcolors

def print_warning(msg: str):
    print(f"{bcolors.WARNING}{msg}{bcolors.ENDC}")

def print_success(msg: str):
    print(f"{bcolors.OKGREEN}{msg}{bcolors.ENDC}")

def print_bold(msg: str):
    print(f"{bcolors.BOLD}{msg}{bcolors.ENDC}")


def fuzzy_match_name(actual_name: str, other_name_start: str):
        if actual_name is None or other_name_start is None:
            return False
        if len(actual_name) == 0 or len(other_name_start) == 0:
            return False
        name_lower = actual_name.casefold()
        other_lower = other_name_start.casefold()
        return name_lower.startswith(other_lower)