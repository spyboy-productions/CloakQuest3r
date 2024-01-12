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