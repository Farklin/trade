
import time 
from app.Parsing.Parsing import Parsing
from app.Base.Base import Base

class QuotekexBror(Parsing):
    
    def inisialization(self):
        # self.driver.execute_script("window.open('about:blank', 'tab2');") 
        self.driver.get(self.url)

    def pairClick(self):
        time.sleep(3)
        element = self.driver.find_element_by_css_selector('.pair-information')
        self.driver.execute_script("arguments[0].click();", element)

    def getText(self): 
        from bs4 import BeautifulSoup

        time.sleep(2)
        bs = BeautifulSoup( self.driver.page_source , 'html.parser' )
        price = bs.select('.modal-pair-information__body-value')[0].text
        print(price)
        self.savePriceBase(price) 
        return price 
    
    def savePriceBase(self, price):
        base = Base() 
        base.insert('INSERT INTO price (site, price) VALUES ("'+self.url+'" ,  '+price+' )' )

    def getOnlinePrice(self):
        mas = [] 
        i = 0 
        while i < 10:
            mas.append(float(self.getText()))
            i += 1 

        return mas

