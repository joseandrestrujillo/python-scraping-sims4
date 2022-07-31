import requests
from bs4 import BeautifulSoup

class pages:
    def getPage(url):
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
        return BeautifulSoup(requests.get(url=url, headers=headers).content, 'html5lib')