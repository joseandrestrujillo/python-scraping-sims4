from scraping.scrapData import Scraper
from database.controller import controller
from decouple import config

url = config('URL_SCRAPING')
print(Scraper(url).getData())

