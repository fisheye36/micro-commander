from conf import settings
import logger

class InsertService:
    def __init__(self, analyserSettings):
        self.__analyserSettings = analyserSettings
        self.__explicit = settings['analysersettings']['explicit']
        self.__finalList = []

    def _appendSpaceIfNeeded(self):
        if self.__analyserSettings.getAutoSpace():
            self.__finalList.append(' ')

    def _deleteSpacesIfNeeded(self):
        if self.__analyserSettings.getAutoSpace() and len(self.__finalList) > 0:
            del self.__finalList[-1]

        for i, word in enumerate(self.__finalList):
            if self.__analyserSettings.getAutoSpace() and i > 0 and (word == '.' or word == ','):
                del self.__finalList[i - 1]

    def _processWordAsExplicit(self, word):
        self.__finalList.append(word)
        self._appendSpaceIfNeeded()
    
    def _processWord(self, word):
        if word == self.__explicit:
            self.__analyserSettings.setExplicit()
        else:
            if word in settings['keyboard_mapping'].keys():
                self.__finalList.append(settings['keyboard_mapping'][word])
            else:
                self.__finalList.append(word)
            self._appendSpaceIfNeeded()

    def process(self, text):
        for word in text.split():
            if self.__analyserSettings.getExplicit():
                self._processWordAsExplicit(word)
            else:
                self._processWord(word)
        self._deleteSpacesIfNeeded()

        return self.__finalList

if __name__ == "__main__":
    pass