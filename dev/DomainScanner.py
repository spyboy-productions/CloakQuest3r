import requests
import ssl
import socket
import threading
import time
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from colorama import init, Fore, Style
import pandas as pd
from bs4 import BeautifulSoup
from typing import Optional, Dict, Union
from datetime import datetime
from enums.cloudflare_status import CloudflareStatus
from config import *

init()


class DomainScanner:
    def __init__(self, domain):
        self.domain = domain
        self.web_server = self.detect_web_server()
        self.subdomains_found = []
        self.ssl_certificate_info_list = []
        self.real_ips_list = []
        self.historical_ips_list = []
        self.lock = threading.Lock()
        self.all_results = []

    def is_using_cloudflare(self, domain: str) -> CloudflareStatus:
        """
        Checks if a given domain is using Cloudflare based on the response headers.

        Args:
            domain (str): The domain to check for Cloudflare usage.

        Returns:
            CloudflareStatus: Enum value indicating whether Cloudflare is detected or not.
        """
        try:
            response = requests.head(f"https://{domain}", timeout=5)
            headers = response.headers

            if "server" in headers and "cloudflare" in headers["server"].lower():
                print("Cloudflare detected!")
                return CloudflareStatus.DETECTED

            if "cf-ray" in headers or "cloudflare" in headers:
                print("Cloudflare detected!")
                return CloudflareStatus.DETECTED

        except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
            pass

        print("Cloudflare not detected!")
        return CloudflareStatus.NOT_DETECTED

    def detect_web_server(self) -> str:
        """
        Detects the web server of a given domain by sending a HEAD request.

        Args:
            domain (str): The domain to detect the web server for.

        Returns:
            str: The detected web server or "UNKNOWN" if the detection fails.
        """
        try:
            response = requests.head(f"http://{self.domain}", timeout=5)
            server_header = response.headers.get("Server")
            if server_header:
                return server_header.strip()
        except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
            pass

        return "UNKNOWN"

    def get_real_ip(self, host: str) -> Optional[str]:
        """
        Get the real IP address of a given host.

        Args:
            host (str): The host to retrieve the IP address for.

        Returns:
            Optional[str]: The real IP address if found, None otherwise.
        """
        try:
            real_ip = socket.gethostbyname(host)
            return real_ip
        except socket.gaierror:
            return None

    def get_ssl_certificate_info(self, host: str) -> Optional[Dict[str, Union[str, datetime]]]:
        """
        Retrieves information about the SSL certificate of the given host.

        Args:
            host (str): The host for which SSL certificate information is requested.

        Returns:
            dict or None: A dictionary containing SSL certificate information, or None if an error occurs.
                The dictionary includes the following keys:
                - "Common Name": Common Name of the certificate.
                - "Issuer": Issuer of the certificate.
                - "Validity Start": Start date of certificate validity.
                - "Validity End": End date of certificate validity.
        """
        try:
            context = ssl.create_default_context()
            with context.wrap_socket(socket.socket(), server_hostname=host) as sock:
                sock.connect((host, 443))
                certificate_der = sock.getpeercert(True)

            certificate = x509.load_der_x509_certificate(certificate_der, default_backend())

            # Extract relevant information from the certificate
            common_name = certificate.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
            issuer = certificate.issuer.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value
            validity_start = certificate.not_valid_before
            validity_end = certificate.not_valid_after

            return {
                "Common Name": common_name,
                "Issuer": issuer,
                "Validity Start": validity_start,
                "Validity End": validity_end,
            }
        except Exception as e:
            print(f"{Fore.RED}Error extracting SSL certificate information: {e}{Fore.RESET}")
            return None

    def find_subdomains_with_ssl_analysis(self, domain: str, filename: str, timeout: int = 20):
        """
        Finds subdomains and performs SSL certificate analysis for each subdomain.

        Args:
            domain (str): The main domain.
            filename (str): The file containing subdomains to scan.
            timeout (int): Timeout for HTTP requests in seconds (default is 20).

        Returns:
            None
        """
        subdomains_found = []
        subdomains_lock = threading.Lock()

        # subdomain scanning...

        def check_subdomain(subdomain: str):
            subdomain_url = f"https://{subdomain}.{domain}"

            try:
                response = requests.get(subdomain_url, timeout=timeout)
                if response.status_code == 200:
                    with subdomains_lock:
                        subdomains_found.append(subdomain_url)
                        print(f"{Fore.GREEN}Subdomain Found \u2514\u27A4: {subdomain_url}{Fore.RESET}")
            except requests.exceptions.RequestException as e:
                if "Max retries exceeded with url" in str(e):
                    pass

        with open(filename, "r") as file:
            subdomains = [line.strip() for line in file.readlines()]

        print(f"\n{Fore.YELLOW}Starting threads...")
        start_time = time.time()

        threads = []
        for subdomain in subdomains:
            thread = threading.Thread(target=check_subdomain, args=(subdomain,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\n{Fore.GREEN} \u2514\u27A4 {Fore.CYAN}Total Subdomains Scanned:{Fore.WHITE} {len(subdomains)}")
        print(f"{Fore.GREEN} \u2514\u27A4 {Fore.CYAN}Total Subdomains Found:{Fore.WHITE} {len(subdomains_found)}")
        print(f"{Fore.GREEN} \u2514\u27A4 {Fore.CYAN}Time taken:{Fore.WHITE} {elapsed_time:.2f} seconds")

        for subdomain in subdomains_found:
            subdomain_parts = subdomain.split('//')
            if len(subdomain_parts) > 1:
                host = subdomain_parts[1]
                real_ip = self.get_real_ip(host)
                if real_ip:
                    self.real_ips_list.append((host, real_ip))
                    print(f"\n{Fore.YELLOW}[+] {Fore.CYAN}Real IP Address of {Fore.GREEN}{host}:{Fore.RED} {real_ip}")

                    # Perform SSL Certificate Analysis
                    ssl_info = self.get_ssl_certificate_info(host)
                    if ssl_info:
                        print(f"{Fore.RED}   [+] {Fore.CYAN}SSL Certificate Information:")
                        for key, value in ssl_info.items():
                            print(f"{Fore.RED}      \u2514\u27A4 {Fore.CYAN}{key}:{Fore.WHITE} {value}")
                        self.ssl_certificate_info_list.append(ssl_info)

        if not self.real_ips_list:
            print(f"{Fore.RED}No real IP addresses found for subdomains.")
        else:
            print("\nTask Complete!!")

    def get_domain_historical_ip_address(self) -> None:
        """
        Retrieves historical IP address information for a domain from Viewdns.

        Returns:
            None
        """
        try:
            url = f"https://viewdns.info/iphistory/?domain={self.domain}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            }
            response = requests.get(url, headers=headers)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find('table', {'border': '1'})

            if table:
                rows = table.find_all('tr')[2:]
                historical_ips = []
                print(
                    f"\n{Fore.GREEN}[+] {Fore.YELLOW}Historical IP Address Info from {Fore.CYAN}Viewdns{Fore.YELLOW} for {Fore.GREEN}{self.domain}:{Fore.WHITE}")
                for row in rows:
                    columns = row.find_all('td')
                    ip_address = columns[0].text.strip()
                    location = columns[1].text.strip()
                    owner = columns[2].text.strip()
                    last_seen = columns[3].text.strip()

                    historical_ips.append({
                        'IP Address': ip_address,
                        'Location': location,
                        'Owner': owner,
                        'Last Seen': last_seen
                    })
                    print(f"{Fore.RED} [+] {Fore.CYAN}IP Address: {Fore.RED}{ip_address}{Fore.WHITE}")
                    print(f"{Fore.YELLOW}  \u2514\u27A4 {Fore.CYAN}Location: {Fore.GREEN}{location}{Fore.WHITE}")
                    print(f"{Fore.YELLOW}  \u2514\u27A4 {Fore.CYAN}Owner: {Fore.GREEN}{owner}{Fore.WHITE}")
                    print(f"{Fore.YELLOW}  \u2514\u27A4 {Fore.CYAN}Last Seen: {Fore.GREEN}{last_seen}{Fore.WHITE}")
                with self.lock:
                    self.historical_ips_list.extend(historical_ips)
            else:
                with self.lock:
                    self.historical_ips_list.append({
                        'IP Address': 'N/A',
                        'Location': 'N/A',
                        'Owner': 'N/A',
                        'Last Seen': 'N/A'
                    })
        except Exception as e:
            print(f"{Fore.RED}Error retrieving historical IP address information: {e}{Fore.RESET}")
            return None

    def run_scan(self):
        print_banners()
        for domain in self.domain:
            cloudflare_ip = self.get_real_ip(domain)
            filename = "wordlist2.txt"
            domain_result = {}

            # Initialize lists for each domain
            subdomains_found = []
            ssl_certificate_info_list = []
            real_ips_list = []
            historical_ips_list = []

            if self.is_using_cloudflare(domain):

                print(f"\n{R}Target Website: {W}{domain}")
                print(f"{R}Visible IP Address: {W}{cloudflare_ip}\n")
                # self.get_domain_historical_ip_address()
                # securitytrails_historical_ip_address(domain)
                print(f"\n{Fore.GREEN}[+] {Fore.YELLOW}Scanning for subdomains.{Fore.RESET}")
                self.find_subdomains_with_ssl_analysis(domain, filename)

            else:
                print(f"{Fore.RED}- Website is not using Cloudflare.")

                technology = self.detect_web_server(domain)
                print(f"\n{Fore.GREEN}[+] {C}Website is using: {Fore.GREEN} {technology}")

            domain_result['Domain'] = domain
            domain_result['Subdomains'] = self.subdomains_found
            domain_result['SSL_Info'] = self.ssl_certificate_info_list
            domain_result['Real_IP'] = self.real_ips_list
            domain_result['Historical_IPs'] = self.historical_ips_list

            self.all_results.append(domain_result)

            result_df = pd.DataFrame(self.all_results)
        return result_df
