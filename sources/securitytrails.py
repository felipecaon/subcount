from utils.utils import color_print
from utils.utils import Colors
from lxml import html
import requests

class Securitytrails:
    def __init__(self, domain):
        self.domain = domain
        self.number_of_subdomains = 0

    def search(self) -> None:
        try:
            domain_name = self.domain

            firefox_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"}

            response = requests.get(f"https://securitytrails.com/domain/{domain_name}/dns", timeout=15, headers=firefox_header)

            tree = html.fromstring(response.content)

            subdomains = tree.xpath('/html/body/div[1]/div[1]/div[3]/main/div[1]/ul/li[4]/a/span/span/text()')

            if subdomains:
                self.number_of_subdomains = subdomains[0].replace(",","")

        except (ConnectionError, TimeoutError):
            color_print("Securitytrails search failed", Colors.FAIL)
        except Exception as e:
            self.number_of_subdomains = "FAIL"

    def get_subdomains(self) -> [int, str]:
        self.search()
        return self.number_of_subdomains