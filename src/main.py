from scraping.scrapData import Scraper
from database.controller import controller
from mailer.makeEmail import makeEmail
from decouple import config

url = config('URL_SCRAPING')
data = Scraper(url).getData()

lastStatus = controller.getLastStatus()
if lastStatus == None:
    lastStatus = (0, -1)
    minorPrice = data["price"]
else:
    if controller.getMinorPrice() == None:
        minorPrice = data["price"]
    else:
        minorPrice = controller.getMinorPrice()[1]

controller.insertStatus(stock=data["stock"], price=data["price"])


# The status change from without stock to with stock
if data["stock"] and lastStatus[0] == 0:
    makeEmail.HaveStock(price=data["price"], minorPrice=minorPrice)

# The status continue with stock
if data["stock"] and lastStatus[0] == 1:
    # The price decreases
    if lastStatus[1] > data["price"]:
        if minorPrice >= data["price"]:
            makeEmail.HistoricalPrice(price=data["price"], minorPrice=minorPrice, prevPrice=lastStatus[1])
        else:
            makeEmail.PriceDecrease(price=data["price"], minorPrice=minorPrice, prevPrice=lastStatus[1])

# The status change from with stock to without stock
if data["stock"] == False and lastStatus[0] == 1:
    makeEmail.BadNews()
    
