
import threading


class Async:

    def __init__(self):
        self.processing = []
         
    def addProcess(self, function, *args):
        x = threading.Thread(target=function, args=args,  daemon=True)
        self.processing.append(x)

    def startProcess(self):
        for processing in self.processing:
            processing.start()  