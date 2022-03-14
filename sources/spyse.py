from utils.utils import color_print
from utils.utils import Colors
from lxml import html
import requests

class Spyse:
    def __init__(self, domain):
        self.domain = domain
        self.number_of_subdomains = 0

    def search(self) -> None:
        try:
            domain_name = self.domain

            firefox_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"}

            response = requests.get(f"https://spyse.com/search?target=domain&query={domain_name}&search_params=%5B%7B%22is_subdomain%22%3A%7B%22operator%22%3A%22eq%22,%22value%22%3A%22true%22%7D%7D%5D", timeout=15, headers=firefox_header)

            tree = html.fromstring(response.content)

            subdomains = tree.xpath("//div[@class='single-search__about']/text()")[0].replace("results", "").replace("About", "").replace(" ", "")

            self.number_of_subdomains = int(subdomains)

        except (ConnectionError, TimeoutError):
            color_print("Spyse search failed", Colors.FAIL)

    def get_subdomains(self) -> int:
        self.search()
        return self.number_of_subdomains