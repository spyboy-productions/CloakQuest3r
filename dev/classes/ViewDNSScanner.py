import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from dev.config import *
from dev.enums.url_headers import *
from dev.exceptions.exceptions import Custom403Exception

class ViewDNSScanner:
    def __init__(self, domain):
        self.domain = domain
        self.data = []

    def get_html_soup(self, url, headers):
        try:

            response = requests.get(url, headers=headers)
            if response.status_code == 403:
                raise Custom403Exception("Access Forbidden. Check your credentials or permissions.")

            response.raise_for_status()
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            print(f'Response code: {response.status_code}')
            return None

    def ip_address_row_parser(self, row):
        columns = row.find_all('td')
        ip_address = columns[0].text.strip()
        location = columns[1].text.strip()
        owner = columns[2].text.strip()
        last_seen = columns[3].text.strip()
        print(f"\n{R} [+] {C}IP Address: {R}{ip_address}{W}")
        print(f"{Y}  \u2514\u27A4 {C}Location: {G}{location}{W}")
        print(f"{Y}  \u2514\u27A4 {C}Owner: {G}{owner}{W}")
        print(f"{Y}  \u2514\u27A4 {C}Last Seen: {G}{last_seen}{W}")

        self.data.append({
            'IP Address': ip_address,
            'Location': location,
            'Owner': owner,
            'Last Seen': last_seen
        })

    def get_domain_historical_ip_address(self):
        try:
            VIEWDNS_HEADERS = {
                "User-Agent": generate_random_ua(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            }
            VIEWDNS_URL = "https://viewdns.info/iphistory/"

            headers = VIEWDNS_HEADERS
            url = f"{VIEWDNS_URL}?domain={self.domain}"

            print('headers', headers)
            print('url', url)

            soup = self.get_html_soup(url, headers)
            table = soup.find('table', {'border': '1'})
            if table:
                rows = table.find_all('tr')[2:]
                print(f"\n{Fore.GREEN}[+] {Fore.YELLOW}Historical IP Address Info from {C}Viewdns{Y} for {Fore.GREEN}{self.domain}:{W}")
                for row in rows:
                    self.ip_address_row_parser(row)
            else:
                print(f"{Fore.RED}Error extracting Historical IP Address information from ViewDNS{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Exception: {e}{Fore.RESET}")

    def run_scan(self):
        self.get_domain_historical_ip_address()