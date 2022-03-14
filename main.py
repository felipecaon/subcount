import optparse
from sources.omnisint import Omnisint
from sources.anubis import Anubis
from sources.securitytrails import Securitytrails
from sources.spyse import Spyse
from utils.utils import color_print
from utils.utils import Colors

def menu():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--domain', dest="domain", help='ex: google.com')

    options, args = parser.parse_args()
    globals().update(locals())


menu()

if options.domain:
    domain = options.domain

    omnisint = Omnisint(domain)
    anubis = Anubis(domain)
    securitytrails = Securitytrails(domain)
    spyse = Spyse(domain)

    omnisint_subdomains = omnisint.get_subdomains()
    anubis_subdomains= anubis.get_subdomains()
    securitytrails_subdomains = securitytrails.get_subdomains()
    spyse_subdomains = spyse.get_subdomains()

    print(f"{domain} - Omnisint: {omnisint_subdomains}, Anubis: {anubis_subdomains}, Securitytrails: {securitytrails_subdomains}, Spyse: {spyse_subdomains}")


