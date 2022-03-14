class Colors:
    HEADER = '\033[95m'
    OK = '\033[94m'
    FAIL = '\033[91m'
    SUCCESS = '\033[92m'
    RESET = '\033[0m'
    WARNING = '\033[93m'
    BOLD = '\033[1m'

def color_print(title: str = "", color_type="") -> None:
    print(f"[{color_type}{title}{Colors.RESET}]")