import requests

url = 'https://www.instant-gaming.com/es/12141-comprar-origin-los-sims-4-anos-high-school-pc-mac-juego-origin/'

r = requests.get(url)

print(r.content)

