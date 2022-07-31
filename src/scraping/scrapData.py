from .page import pages

class Scraper:
    def __init__(self, url) -> None:
        self.page = pages.getPage(url)
    def getData(self):
        hasStock = len(self.page.find_all('div', attrs= {'class':'nostock'})) == 0 

        if hasStock:
            amountInfo = self.page.find_all('div', attrs= {'class':'panel item wide'})[0].find_all('div', attrs= {'class':'amount'})[0]
            price = float(amountInfo.find_all('div', attrs= {'class':'total'})[0].text.replace("â‚¬", ""))
            result = {
                "stock": hasStock,
                "price": price ,
            }
        else:
            result = {
                "stock": hasStock,
                "price": -1,
            }

        return result

