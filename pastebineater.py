#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from urllib.parse import urlparse
try:
    import requests
    from bs4 import BeautifulSoup
except:
    os.system('python -m pip install -U requests --user')
    os.system('python -m pip install -U beautifulsoup4 --user')
    print('Agora você têm as dependências, cusão')
    exit()


def linkRestriction(link):
    if "url?q=" in link and not "webcache" in link:
        return True
    return False


def writeFile(name, text):
# definir um diretório para escrita segura
    try:
        fout = open(name, 'a')
        fout.write(text)
        fout.close()
        return True
    except Exception:
        return False


PROXIES = {
    'http': '78.133.206.129:4145',
    'https': '192.169.233.11:57260'
}
queries = open('query', 'r')
num_results = 8

GOOGLE_QUERY = "https://www.google.com/search?q={}&num={}&as_qdr=d"
PASTEBIN_RAW = "https://pastebin.com/raw{0}"

for query in queries:
    search = query.strip('\n').replace(' ', '+')
    URL = GOOGLE_QUERY.format(search, str(num_results))
    r = requests.get(URL)
    print("[+] URL: %s : STATUS CODE: %s" % (URL, r.status_code))
    if r.ok():
        for link in BeautifulSoup(r.content, 'html.parser').find_all('a'):
            href = link.get('href')
            if linkRestriction(href):
                grabber = href.split("?q=")[1].split("&sa=U")[0]
                x = urlparse(grabber)
                data = requests.get(PASTEBIN_RAW.format(x[2])).text
                if writeFile("PasteBin_" + x[2].strip('/'), data):
                    print('[+] URL> {}\n{}\n'.format(grabber, data))
queries.close()
