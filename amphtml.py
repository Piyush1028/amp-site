import requests
from bs4 import BeautifulSoup

r=requests.get('http://www.theguardian.com/weather/2016/jan/22/monster-snow-storm-bears-down-on-us-east-coast-threatening-chaos')
data=r.text
soup=BeautifulSoup(data)

for link in soup.find_all(rel='amphtml'):
    print(link.get('href'))
    