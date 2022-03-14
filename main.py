import optparse, multiprocessing
from sources.omnisint import Omnisint
from sources.anubis import Anubis
from sources.securitytrails import Securitytrails
from sources.spyse import Spyse
from utils.utils import check_if_domain_is_valid, color_print, Colors

def menu():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--domain', dest="domain", help='ex: google.com')
    parser.add_option('-l', '--list', dest="list", help='ex: list.txt')
    parser.add_option('-t', '--threads', dest="threads", help='Number of threads, default is 5', default=20)

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

    print(f"{domain} > Omnisint: {omnisint_subdomains}, Anubis: {anubis_subdomains}, Securitytrails: {securitytrails_subdomains}, Spyse: {spyse_subdomains}")

menu()

if options.list:
    parallelism = multiprocessing.Pool(options.threads)

    f = open(options.list, "r")
    domains = map(str.strip, f.readlines())
    try:
        parallelism.map(count_subdomains, domains)
        parallelism.close()
        parallelism.join()
    except UnboundLocalError:
        pass
    except KeyboardInterrupt:
        sys.exit(0)


if options.domain:
    count_subdomains(options.domain)
