
import time 
from app.Parsing.Parsing import Parsing
from app.Base.Base import Base

class AlpariforexSite(Parsing):
    
    def inisialization(self):
        # self.driver.execute_script("window.open('about:blank', 'tab2');") 
        self.driver.get(self.url)

    
