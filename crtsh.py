#!/usr/bin/env python3
import sys
import argparse
import requests

BASE_URL = "https://crt.sh/?q={}&output=json"

def parser_error(errmsg):
    print(f"Usage: python3 {sys.argv[0]} [Options] use -h for help")
    print(f"Error: {errmsg}")
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(
        epilog=f'Example:\r\npython3 {sys.argv[0]} -d google.com'
    )
    parser.error = parser_error
    parser.add_argument('-d', '--domain',
                        help='Specify Target Domain to get subdomains from crt.sh',
                        required=True)
    parser.add_argument('-r', '--recursive',
                        help='Do recursive search for subdomains',
                        action='store_true')
    parser.add_argument('-w', '--wildcard',
                        help='Include wildcard in output',
                        action='store_true')
    return parser.parse_args()

def fetch_subdomains(domain):
    try:
        response = requests.get(BASE_URL.format(domain), timeout=25)
        response.raise_for_status()
        jsondata = response.json()
        return jsondata
    except requests.RequestException as e:
        print(f"Error fetching data from CRT.SH: {e}")
        return []

def process_subdomains(domain, recursive=False, wildcard=False):
    subdomains = set()
    wildcard_subdomains = set()

    def add_subdomain(subdomain):
        if '*' in subdomain:
            wildcard_subdomains.add(subdomain)
        else:
            subdomains.add(subdomain)

    jsondata = fetch_subdomains(domain)
    for entry in jsondata:
        name_value = entry.get('name_value', '')
        subnames = name_value.splitlines()
        for subname in subnames:
            add_subdomain(subname.strip())

    if recursive:
        for wildcard_subdomain in list(wildcard_subdomains):
            wildcard_subdomain_encoded = wildcard_subdomain.replace('*', '%25')
            jsondata_recursive = fetch_subdomains(wildcard_subdomain_encoded)
            for entry in jsondata_recursive:
                name_value = entry.get('name_value', '')
                subnames = name_value.splitlines()
                for subname in subnames:
                    add_subdomain(subname.strip())

    if wildcard:
        subdomains.update(wildcard_subdomains)

    return subdomains

if __name__ == "__main__":
    args = parse_args()
    subdomains = process_subdomains(args.domain, args.recursive, args.wildcard)

    for subdomain in sorted(subdomains):  # Sort subdomains alphabetically
        print(subdomain)
