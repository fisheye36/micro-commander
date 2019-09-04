from conf import settings
from analyser.insertservice import InsertService

class CommandService(InsertService):
    def __init__(self, analyserSettings):
        InsertService.__init__(self, analyserSettings)
        self.__analyserSettings = analyserSettings
        self.__finalList = []

    def _processAsCommand(self, words):
        command = ''.join(words)
        if command in settings.active()['commands'].keys():
            self.__finalList = settings.active()['commands'][command]
            return True
        return False


    def _processAsAnalyserSettings(self, listOfWords):
        command = ''.join(listOfWords).lower()
        if command == settings['analysersettings']['autospace']:
            self.__analyserSettings.switchAutoSpace()
            return True
        return False

    def process(self, text):
        listOfWords = text.split()
        del listOfWords[0]
        words = super().process(' '.join(listOfWords))
        
        if self._processAsAnalyserSettings(listOfWords):
            self.__finalList = []
        elif self._processAsCommand(words):
            pass
        return self.__finalList

if __name__ == "__main__":
    pass