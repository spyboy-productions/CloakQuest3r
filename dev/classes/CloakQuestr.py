import pandas as pd
from dev.classes.HeaderScanner import HeaderScanner
from dev.classes.SubDomainScanner import SubDomainScanner
from dev.classes.ViewDNSScanner import ViewDNSScanner
from dev.classes.SecurityTrailsScanner import SecurityTrailsScanner


class CloakQuestr:
    def __init__(self, domains):
        self.domains = domains
        self.result_dict = {'dns': pd.DataFrame(), 'domains': pd.DataFrame(), 'securitytrails': pd.DataFrame()}

    def scan_headers(self, domain):
        header_scanner = HeaderScanner(domain)
        webserver = header_scanner.run_scan()
        return webserver

    def scan_dns(self, domain):
        dns_scanner = ViewDNSScanner(domain)
        dns_scanner.run_scan()
        df = pd.DataFrame(dns_scanner.data)
        df['domain'] = domain
        df['webserver'] = self.scan_headers(domain)
        return df


    def scan_subdomains(self, domain):
        subdomain_scanner = SubDomainScanner(domain)
        subdomain_scanner.run_scan()
        df = pd.DataFrame(subdomain_scanner.data)
        df['domain'] = domain
        df['webserver'] = self.scan_headers(domain)
        return df

    def scan_security_trails(self, domain):
        security_trails_scanner = SecurityTrailsScanner(domain)
        security_trails_scanner.securitytrails_historical_ip_address(domain)
        df = pd.DataFrame(security_trails_scanner.data)
        df['domain'] = domain
        df['webserver'] = self.scan_headers(domain)
        return df

    def run_scan(self, as_df=True, as_csv=False):
        if isinstance(self.domains, str):
            self.domains = [self.domains]

        for domain in self.domains:
            self.result_dict['dns'] = pd.concat([self.result_dict['dns'], self.scan_dns(domain)], ignore_index=True)
            self.result_dict['domains'] = pd.concat([self.result_dict['domains'], self.scan_subdomains(domain)], ignore_index=True)
            self.result_dict['securitytrails'] = pd.concat([self.result_dict['securitytrails'], self.scan_security_trails(domain)], ignore_index=True)
        return self.result_dict