import optparse
from sources.omnisint import Omnisint
from sources.anubis import Anubis
from sources.securitytrails import Securitytrails
from sources.spyse import Spyse
from utils.utils import check_if_domain_is_valid
from utils.utils import color_print
from utils.utils import Colors

def menu():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--domain', dest="domain", help='ex: google.com')
    parser.add_option('-l', '--list', dest="list", help='ex: list.txt')

    options, args = parser.parse_args()
    globals().update(locals())

def count_subdomains(domain: str) -> None:
    domain = domain

    if not check_if_domain_is_valid(domain):
        color_print(f"> Domain {domain} is not valid", Colors.FAIL)
        return

    omnisint = Omnisint(domain)
    anubis = Anubis(domain)
    securitytrails = Securitytrails(domain)
    spyse = Spyse(domain)

    omnisint_subdomains = omnisint.get_subdomains()
    anubis_subdomains= anubis.get_subdomains()
    securitytrails_subdomains = securitytrails.get_subdomains()
    spyse_subdomains = spyse.get_subdomains()

    print(f"{domain} - Omnisint: {omnisint_subdomains}, Anubis: {anubis_subdomains}, Securitytrails: {securitytrails_subdomains}, Spyse: {spyse_subdomains}")

menu()

if options.list:
    f = open(options.list, "r")
    domains = f.readlines()
    for d in domains:
        count_subdomains(d.strip())

if options.domain:
    count_subdomains(options.domain)
