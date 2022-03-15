## Description

Give a subdomain or list and subcount will retrieve only the amount of records of said domain

## Sources

- Omnilist
- Spyse
- SecurityTrails
- Anubis

## Usage

```bash
Options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain=DOMAIN
                        ex: google.com
  -l LIST, --list=LIST  ex: list.txt
  -t THREADS, --threads=THREADS
                        Number of threads, default is 20
```

## Output 

```bash
$ python3 main.py -d google.com
google.com > Omnisint: 34837, Anubis: 5137, Securitytrails: 1M+, Spyse: 52514
```