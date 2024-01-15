from enum import Enum
from dev.config import  read_config


class ViewDNS:
    def __init__(self):
        VIEWDNS_HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        }
        VIEWDNS_URL = "https://viewdns.info/iphistory/"

    def set_domain(self, domain):
        self.domain = domain

    def get_url(self):
        return f"{self.VIEWDNS_URL}?domain={self.domain}"



class SecurityTrails(Enum):
    SECURITYTRAILS_HEADERS = {
        "accept": "application/json",
        "APIKEY": read_config()
    }
    def set_domain(self, domain):
        self.SECURITYTRAILS_URL = f"https://api.securitytrails.com/v1/history/{domain}/dns/a"
    pass