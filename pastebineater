#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
proxies = {
    'https':'192.169.233.11:57260',
    'http': '78.133.206.129:4145'
        }
#https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters
fin = open('query','r')
num_results=8

for query in fin:
  searc=query.strip('\n')
  search=searc.replace(' ','+')
  #URL="https://www.google.com/search?q={}&num={}".format(search,str(num_results))
  # Time based search, previus 24h
  URL="https://www.google.com/search?q={}&num={}&as_qdr=d".format(search,str(num_results))
  # Previus seven days
#  URL="https://www.google.com/search?q={}&num={}&as_qdr=w".format(search,str(num_results))
  # Previus month
#  URL="https://www.google.com/search?q={}&num={}&as_qdr=m".format(search,str(num_results))
  #r=requests.get(URL,proxies=proxies)
  r=requests.get(URL)
  print "[+] URL: %s : STATUS CODE: %s" %( URL, r.status_code)
  html=r.content
  soup=BeautifulSoup(html,'html5lib')
  links=soup.find_all('a')
  filer=''
  for link in links:
    link_href=link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
      grabber = link.get('href').split("?q=")[1].split("&sa=U")[0]
      x = urlparse(grabber)
      data = requests.get("https://pastebin.com/raw{0}".format(x[2])).text
      encdata = data.encode('utf-8')
      massdata = x[2].strip('/')
      try:
        fout = open(massdata,'a')
        fout.write(data)
        fout.close()
      except Exception as error:
        continue
      filer+='[+] URL> {}\n\n{}\n\n\n'.format(grabber, data)
      print filer
fin.close()
