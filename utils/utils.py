class Colors:
    HEADER = '\033[95m'
    OK = '\033[94m'
    FAIL = '\033[91m'
    SUCCESS = '\033[92m'
    RESET = '\033[0m'
    WARNING = '\033[93m'
    BOLD = '\033[1m'

def color_print(title: str = "", text: str = "", color_type="") -> None:
    print(f"[{Colors.OK}{title}{Colors.RESET}] {color_type}{text}{Colors.RESET}")