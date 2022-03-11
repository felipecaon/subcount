import optparse
from sources.omnisint import Omnisint
from sources.anubis import Anubis

def menu():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--domain', dest="domain", help='ex: google.com')

    options, args = parser.parse_args()
    globals().update(locals())


menu()

# security trails
# https://dnsrepo.noc.org/?search=yahoo.com.br
# https://dns.bufferover.run/dns?q=uber.com
# https://jldc.me/anubis/subdomains

if options.domain:
    domain = options.domain

    omnisint = Omnisint(domain)
    anubis = Anubis(domain)

    omnisint.get_subdomains()
    anubis.get_subdomains()