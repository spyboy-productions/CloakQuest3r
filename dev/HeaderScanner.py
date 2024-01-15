import requests
from enums.cloudflare_status import CloudflareStatus


class HeaderScanner:
    def __init__(self, domain):
        self.domain = domain

    def get_headers(self):
        try:
            response = requests.head(f"https://{self.domain}", timeout=5)
        except (requests.exceptions.RequestException,
                requests.exceptions.ConnectionError):
                pass
        return response.headers

    def detect_cloudflare(self, headers):
        if "server" in headers and "cloudflare" in headers["server"].lower():
            print("Cloudflare detected!")
            return CloudflareStatus.DETECTED
        if "cf-ray" in headers or "cloudflare" in headers:
            print("Cloudflare detected!")
            return CloudflareStatus.DETECTED

    def detect_webservers(self, headers):
        server_header = headers.get("Server")
        if server_header:
            return server_header.strip()
        return None

    def run_scan(self):
        headers = self.get_headers()
        if headers:
            cloudflare_status = self.detect_cloudflare(headers)
            if cloudflare_status == CloudflareStatus.DETECTED:
                webserver = self.detect_webservers(headers)
                return webserver
            return None