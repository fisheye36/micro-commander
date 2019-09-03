from conf import settings
from copy import deepcopy
from analyser.insertservice import InsertService
import importlib

class Analyser:
    def __init__(self):
        self.finalList = []
        self.activeService = InsertService(self)

    def setService(self, text):
        wordList = text.split()
        if wordList[0] in settings.active()['servicemapping'].keys():
            serviceName = settings.active()['servicemapping'][wordList[0]]
            module = importlib.import_module("analyser." + serviceName.lower())
            service = getattr(module, serviceName)
            self.activeService = service(self)
        else:
            self.activeService = InsertService(self)

    def analyse(self, text):
        self.setService(text)
        self.finalList = self.activeService.process(text)
        return self.finalList

if __name__ == "__main__":
    pass