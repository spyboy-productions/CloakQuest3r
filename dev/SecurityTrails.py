from config import read_config
from config import *
from enums.url_headers import *
import requests
from colorama import Fore

class SecurityTrailsScanner:
    def __init__(self, domain):
        self.domain = domain

    def security_trails_record_parser(self, record):
        ip = record["values"][0]["ip"]
        first_seen = record["first_seen"]
        last_seen = record["last_seen"]
        organizations = record["organizations"][0]
        print(f"\n{R} [+] {C}IP Address: {R}{ip}{W}")
        print(f"{Y}  \u2514\u27A4 {C}First Seen: {G}{first_seen}{W}")
        print(f"{Y}  \u2514\u27A4 {C}Last Seen: {G}{last_seen}{W}")
        print(f"{Y}  \u2514\u27A4 {C}Organizations: {G}{organizations}{W}")

    def securitytrails_historical_ip_address(self):
        if read_config() :

            # functionalize this in order to be a generic enumeration method
            securitytrails_instance = SecurityTrails()
            securitytrails_instance.set_domain(self.domain)

            url = SecurityTrails.SECURITYTRAILS_URL
            headers = SecurityTrails.SECURITYTRAILS_HEADERS

            try:
                response = requests.get(url, headers=headers)
                data = response.json()
                print(f"\n{Fore.GREEN}[+] {Fore.YELLOW}Historical IP Address Info from {C}SecurityTrails{Y} for {Fore.GREEN}{self.domain}:{W}")
                for record in data['records']:
                    self.security_trails_record_parser(record)
            except:
                print(f"{Fore.RED}Error extracting Historical IP Address information from SecurityTrails{Fore.RESET}")
                None
        else:
            print(f"{Fore.RED}Please add your {C}SecurityTrails{Fore.RED} API Key in config.ini file{Fore.RESET}")
            None