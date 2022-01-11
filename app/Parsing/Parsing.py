from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import os 

class Parsing:
    
    def __init__(self, url): 
        self.url = url 

    # инициализация chrome         
    def auth(self, unic):
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir="+os.getcwd() + unic +"selenium") 
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

        #self.driver.execute_script("document.body.style.zoom='80%'")
