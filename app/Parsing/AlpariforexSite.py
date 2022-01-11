
import time 
from app.Parsing.Parsing import Parsing
from app.Base.Base import Base

class AlpariforexSite(Parsing):
    
    def inisialization(self):
        # self.driver.execute_script("window.open('about:blank', 'tab2');") 
        self.driver.get(self.url)

    def getPrice():
        from bs4 import BeautifulSoup

        time.sleep(4)
        bs = BeautifulSoup( self.driver.page_source , 'html.parser' )
        price = bs.select('.bali-asset-row.asset-item-row')[0].text
        print(price)
        return price 
    
