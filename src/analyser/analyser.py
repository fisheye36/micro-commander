from conf import settings
from copy import deepcopy
from analyser.insertservice import InsertService
from analyser.analysersettings import AnalyserSettings
import importlib

class Analyser:
    def __init__(self):
        self.finalList = []
        self.__analyserSettings = AnalyserSettings()

    def _setService(self, text):
        wordList = text.split()
        if wordList[0].lower() in settings['servicemapping'].keys():
            serviceName = settings['servicemapping'][wordList[0].lower()]
            module = importlib.import_module('analyser.' + serviceName.lower())
            service = getattr(module, serviceName)
            self.activeService = service(self.__analyserSettings)
        else:
            self.activeService = InsertService(self.__analyserSettings)

    def analyse(self, text):
        self._setService(text)
        self.finalList = self.activeService.process(text)
        return self.finalList

if __name__ == "__main__":
    pass