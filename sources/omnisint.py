from utils.utils import color_print
from utils.utils import Colors
from json import dumps, loads
import requests

class Omnisint:
    def __init__(self, domain):
        self.domain = domain
        self.number_of_subdomains = 0

    def search(self) -> None:
        try:
            domain_name = self.domain

            number_of_subdomains = len(requests.get(f"https://sonar.omnisint.io/tlds/{domain_name}", timeout=15).json())

            self.number_of_subdomains = number_of_subdomains

        except (ConnectionError, TimeoutError):
            color_print("Omnisint search failed", Colors.FAIL)

    def get_subdomains(self) -> int:
        self.search()
        return self.number_of_subdomains