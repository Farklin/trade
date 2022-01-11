from manager import ParsingBirzhi, Canvas
from asinc import Async
from app.Parsing.QuotekexBror import QuotekexBror
from threading import Thread

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

url = 'https://quotex-broker.com/ru/demo-trade'
parsing = QuotekexBror(url)
parsing.auth()
parsing.inisialization()
parsing.pairClick()
result = parsing.getOnlinePrice()
print(result)