from dev.config import read_config
from dev.config import generate_random_ua

class ViewDNS:

    VIEWDNS_HEADERS = {
        "User-Agent": generate_random_ua(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }
    VIEWDNS_URL = "https://viewdns.info/iphistory/"


class SecurityTrails:

    SECURITYTRAILS_HEADERS = {
        "accept": "application/json",
        "APIKEY": read_config()
    }

    SECURITYTRAILS_URL = "https://api.securitytrails.com/v1/history/{domain}/dns/a"