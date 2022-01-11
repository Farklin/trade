
from app.Parsing.QuotekexBror import QuotekexBror
from app.Parsing.AlpariforexSite import AlpariforexSite
from threading import Thread
from app.Async.Async import Async

import time

# def parsing(): 
#     url = 'https://quotex-broker.com/ru/demo-trade'

#     parsing = QuotekexBror(url)
#     parsing.auth()
#     parsing.pairClick()
#     result = parsing.getOnlinePrice()
#     print(result)


# for i in range(4):
#     time.sleep(5)
#     th = Thread(target=parsing, args=( ))
#     th.start()

def qumo(): 
    url = 'https://quotex-broker.com/ru/demo-trade'
    parsing = QuotekexBror(url)
    parsing.auth('12')
    parsing.inisialization() 
    parsing.pairClick()
    parsing.getOnlinePrice()

def alpa():
    url = 'https://alpariforex.site/ru/fix-contracts/'
    parsing = AlpariforexSite(url)
    parsing.auth('13')
    parsing.inisialization()

ass = Async()
ass.addProcess(qumo)
ass.addProcess(alpa)
ass.startProcess() 