import subprocess
import socket
import ssl
from colorama import Fore, Back, Style
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from config import *
class SubDomainScanner:
    def __init__(self, domain):
        self.domain = domain

    def get_domain_names(self):
        """
        Uses crt.sh to get a list of domain names for a given domain.
        """
        url = f"https://crt.sh/?q=%{self.domain}%&output=json"
        command = f'curl -s "{url}" | jq -r ".[].name_value" | sed "s/*.//g" | sort -u'

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode == 0:
            cleaned_output = output.decode('utf-8').strip()
            domain_names = cleaned_output.split('\n')
            return domain_names
        else:
            error_message = error.decode('utf-8').strip()
            print(f"Error executing command: {error_message}")
            return None

    def get_real_ip(self, timeout=5):
        try:
            if not isinstance(self.domain, str) or not self.domain:
                raise ValueError("Invalid hostname")

            # Use getaddrinfo for IPv4 addresses only
            addrinfo = socket.getaddrinfo(self.domain, None, socket.AF_INET, socket.SOCK_STREAM)

            # Return the first IPv4 address
            for family, _, _, _, sockaddr in addrinfo:
                ip_address = sockaddr[0]
                return ip_address

        except (socket.gaierror, ValueError) as e:
            print(f"Error: {e}")
            return None

        except socket.error as e:
            print(f"Socket error: {e}")
            return None

        except Exception as e:
            print(f"Unexpected error: {e}")
            return None


    def get_ssl_certificate_info(self, host):
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

    def run_scan(self):
        domain_list = self.get_domain_names()
        for subdomain in domain_list:
            real_ip = self.get_real_ip(subdomain)
            if real_ip:
                print(f"{Fore.YELLOW}[+] {Fore.CYAN}Real IP Address of {Fore.GREEN}{subdomain}:{Fore.RED} {real_ip}")

                # Perform SSL Certificate Analysis
                ssl_info = self.get_ssl_certificate_info(subdomain)
                if ssl_info:
                    print(f"{Fore.RED}   [+] {Fore.CYAN}SSL Certificate Information:")
                    for key, value in ssl_info.items():
                        print(f"{Fore.RED}      \u2514\u27A4 {Fore.CYAN}{key}:{W} {value}")