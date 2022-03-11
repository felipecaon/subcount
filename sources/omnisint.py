from utils.utils import color_print
from json import dumps, loads
import requests

class Omnisint:
    def __init__(self, domain):
        self.domain = domain
        self.number_of_subdomains = 0
        self.search()

    def search(self) -> None:
        color_print("Omnisint search", "Process started")

        try:
            domain_name = self.domain

            all_sonar_subdomains = []

            number_of_subdomains = len(requests.get(f"https://sonar.omnisint.io/tlds/{domain_name}", timeout=15).json())

            self.number_of_subdomains = number_of_subdomains

        except (ConnectionError, TimeoutError):
            color_print("Omnisint search", "Omnisint search failed - skipping", Colors.FAIL)

    def get_subdomains(self) -> int:
        print(self.number_of_subdomains)