import requests
from bs4 import BeautifulSoup

url = 'https://www.instant-gaming.com/es/9755-comprar-monster-hunter-rise-sunbreak-pc-juego-steam/'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

r = requests.get(url=url, headers=headers)

soup = BeautifulSoup(r.content, 'html5lib')

hasStock = len(soup.find_all('div', attrs= {'class':'nostock'})) == 0 

if hasStock:
    amountInfo = soup.find_all('div', attrs= {'class':'panel item wide'})[0].find_all('div', attrs= {'class':'amount'})[0]
    price = amountInfo.find_all('div', attrs= {'class':'total'})[0].text
    price = float(price.replace("â‚¬", ""))