from re import search

class Colors:
    HEADER = '\033[95m'
    OK = '\033[94m'
    FAIL = '\033[91m'
    SUCCESS = '\033[92m'
    RESET = '\033[0m'
    WARNING = '\033[93m'
    BOLD = '\033[1m'

def color_print(title: str = "", color_type="") -> None:
    print(f"{color_type}{title}{Colors.RESET}")

def check_if_domain_is_valid(domain: str) -> bool:
    _DOMAIN_REGEX = "^(?=.{1,253}\.?$)(?:(?!-|[^.]+_)[A-Za-z0-9-_]{1,63}(?<!-)(?:\.|$)){2,}$"
    if search(_DOMAIN_REGEX, domain):
        return True
    else:
        return False
