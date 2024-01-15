import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from config import *
from enums.url_headers import *

class ViewDNSScanner:
    def __init__(self, domain):
        self.domain = domain

    def get_html_soup(self, url, headers):
        try:
            response = requests.get(url, headers=headers)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except:
            None

    def ip_address_row_parser(row):
        columns = row.find_all('td')
        ip_address = columns[0].text.strip()
        location = columns[1].text.strip()
        owner = columns[2].text.strip()
        last_seen = columns[3].text.strip()
        print(f"\n{R} [+] {C}IP Address: {R}{ip_address}{W}")
        print(f"{Y}  \u2514\u27A4 {C}Location: {G}{location}{W}")
        print(f"{Y}  \u2514\u27A4 {C}Owner: {G}{owner}{W}")
        print(f"{Y}  \u2514\u27A4 {C}Last Seen: {G}{last_seen}{W}")

    def get_domain_historical_ip_address(self):
        try:
            headers = ViewDNS.VIEWDNS_HEADERS
            viewdns_instance = ViewDNS()
            viewdns_instance.set_domain(self.domain)
            url = ViewDNS.VIEWDNS_URL

            soup = self.get_html_soup(url, headers)
            table = soup.find('table', {'border': '1'})
            if table:
                rows = table.find_all('tr')[2:]
                print(f"\n{Fore.GREEN}[+] {Fore.YELLOW}Historical IP Address Info from {C}Viewdns{Y} for {Fore.GREEN}{self.domain}:{W}")
                for row in rows:
                    self.ip_address_row_parser(row)
            else:
                print(f"{Fore.RED}Error extracting Historical IP Address information from ViewDNS{Fore.RESET}")
        except:
            None

    def run_scan(self):
        self.get_domain_historical_ip_address()