import socket
import sys
import ssl
import requests
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from colorama import init, Fore
import threading
import time
from bs4 import BeautifulSoup

twitter_url = 'https://spyboy.in/twitter'
discord = 'https://spyboy.in/Discord'
website = 'https://spyboy.in/'
blog = 'https://spyboy.blog/'
github = 'https://github.com/spyboy-productions/CloakQuest3r'

VERSION = '1.0.4'

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow

banner = r'''
   ___ _             _      ____                 _   _____
  / __\ | ___   __ _| | __ /___ \_   _  ___  ___| |_|___ / _ __
 / /  | |/ _ \ / _` | |/ ///  / / | | |/ _ \/ __| __| |_ \| '__|
/ /___| | (_) | (_| |   </ \_/ /| |_| |  __/\__ \ |_ ___) | |
\____/|_|\___/ \__,_|_|\_\___,_\ \__,_|\___||___/\__|____/|_|
Uncover the true IP address of websites safeguarded by Cloudflare & ohers.
'''

init()

def print_banners():
    """
    prints the program banners
    """
    print(f'{R}{banner}{W}\n')
    print(f'{G}[+] {Y}Version      : {W}{VERSION}')
    print(f'{G}[+] {Y}Created By   : {W}Spyboy')
    print(f'{G} \u2514\u27A4 {Y}Twitter      : {W}{twitter_url}')
    print(f'{G} \u2514\u27A4 {Y}Discord      : {W}{discord}')
    print(f'{G} \u2514\u27A4 {Y}Website      : {W}{website}')
    print(f'{G} \u2514\u27A4 {Y}Blog         : {W}{blog}')
    print(f'{G} \u2514\u27A4 {Y}Github       : {W}{github}\n')

def is_using_cloudflare(domain):
    try:
        response = requests.head(f"https://{domain}", timeout=5)
        headers = response.headers
        if "server" in headers and "cloudflare" in headers["server"].lower():
            return True
        if "cf-ray" in headers:
            return True
        if "cloudflare" in headers:
            return True
    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
        pass

    return False

def detect_web_server(domain):
    try:
        response = requests.head(f"http://{domain}", timeout=5)
        server_header = response.headers.get("Server")
        if server_header:
            return server_header.strip()
    except (requests.exceptions.RequestException, requests.exceptions.ConnectionError):
        pass

    return "UNKNOWN"

def get_ssl_certificate_info(host):
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

def find_subdomains_with_ssl_analysis(domain, filename, timeout=20):
    #if not is_using_cloudflare(domain):
        #print(f"{C}Website is not using Cloudflare. Subdomain scan is not needed.{W}")
        #return

    subdomains_found = []
    subdomains_lock = threading.Lock()

    # subdomain scanning...

    def check_subdomain(subdomain):
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
    print(f"\n{G} \u2514\u27A4 {C}Total Subdomains Scanned:{W} {len(subdomains)}")
    print(f"{G} \u2514\u27A4 {C}Total Subdomains Found:{W} {len(subdomains_found)}")
    print(f"{G} \u2514\u27A4 {C}Time taken:{W} {elapsed_time:.2f} seconds")

    real_ips = []

    for subdomain in subdomains_found:
        subdomain_parts = subdomain.split('//')
        if len(subdomain_parts) > 1:
            host = subdomain_parts[1]
            real_ip = get_real_ip(host)
            if real_ip:
                real_ips.append((host, real_ip))
                print(f"\n{Fore.YELLOW}[+] {Fore.CYAN}Real IP Address of {Fore.GREEN}{host}:{Fore.RED} {real_ip}")

                # Perform SSL Certificate Analysis
                ssl_info = get_ssl_certificate_info(host)
                if ssl_info:
                    print(f"{Fore.RED}   [+] {Fore.CYAN}SSL Certificate Information:")
                    for key, value in ssl_info.items():
                        print(f"{Fore.RED}      \u2514\u27A4 {Fore.CYAN}{key}:{W} {value}")

    if not real_ips:
        print(f"{R}No real IP addresses found for subdomains.")
    else:
        print("\nTask Complete!!\n")
        # for link in subdomains_found:
        # print(link)

def get_real_ip(host):
    try:
        real_ip = socket.gethostbyname(host)
        return real_ip
    except socket.gaierror:
        return None

    
def get_domain_historical_ip_address(domain):
    url = f"https://viewdns.info/iphistory/?domain={domain}"
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
        print(f"\n{Fore.GREEN}[+] {Fore.YELLOW}Historical IP Address Info for {Fore.GREEN}{domain}:{W}")
        for row in rows:
            columns = row.find_all('td')
            ip_address = columns[0].text.strip()
            location = columns[1].text.strip()
            owner = columns[2].text.strip()
            last_seen = columns[3].text.strip()
            print(f"\n{R} [+] {C}IP Address: {R}{ip_address}{W}")
            print(f"{Y}  \u2514\u27A4 {C}Location: {G}{location}{W}")
            print(f"{Y}  \u2514\u27A4 {C}Owner: {G}{owner}{W}")
            print(f"{Y}  \u2514\u27A4 {C}Last Seen: {G}{last_seen}{W}")
    else:
        None


if __name__ == "__main__":
    domain = sys.argv[1]  # pass domain in command-line argument ex: python3 cloakquest3r.py top.gg
    filename = "wordlist2.txt"
    print_banners()
    CloudFlare_IP = get_real_ip(domain)

    print(f"\n{Fore.GREEN}[!] {C}Checking if the website uses Cloudflare{Fore.RESET}\n")

    if is_using_cloudflare(domain):

        print(f"\n{R}Target Website: {W}{domain}")
        print(f"{R}Visible IP Address: {W}{CloudFlare_IP}\n")
        get_domain_historical_ip_address(domain)

        print(f"\n{Fore.GREEN}[+] {Fore.YELLOW}Scanning for subdomains.{Fore.RESET}")
        find_subdomains_with_ssl_analysis(domain, filename)

    else:
        print(f"{Fore.RED}- Website is not using Cloudflare.")
        
        # Determine what technology it is using
        technology = detect_web_server(domain)
        print(f"\n{Fore.GREEN}[+] {C}Website is using: {Fore.GREEN} {technology}")

        # Ask the user if they want to proceed
        proceed = input(f"\n{Fore.YELLOW}> Do you want to proceed? {Fore.GREEN}(yes/no): ").lower()

        if proceed == "yes":
            # Add the functionality for the specific technology here
            print(f"\n{R}Target Website: {W}{domain}")
            print(f"{R}Visible IP Address: {W}{CloudFlare_IP}\n")
            get_domain_historical_ip_address(domain)

            print(f"{Fore.GREEN}[+] {Fore.YELLOW}Scanning for subdomains.{Fore.RESET}")
            find_subdomains_with_ssl_analysis(domain, filename)
        else:
            print(f"{R}Operation aborted. Exiting...{W}")

