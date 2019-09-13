from conf import settings
import logger
from analyser.capitalletters import CapitalLetters

class InsertService:
    def __init__(self, analyserSettings):
        self.__analyserSettings = analyserSettings
        self.__explicit = settings['analysersettings']['explicit']
        self.__switchShift = settings['analysersettings']['switchShift']
        self.__finalList = []

    def _appendCapitalIfNeeded(self):
        if self.__analyserSettings.getCapitalLettersState() == CapitalLetters.OFF:
            self.__finalList[-1] = self.__finalList[-1].lower()
        elif self.__analyserSettings.getCapitalLettersState() == CapitalLetters.AUTO:
            if self.__finalList[-1] == '.':
                self.__analyserSettings.setShift()
                return
        else:
            self.__finalList[-1] = self.__finalList[-1].upper()

        if self.__finalList[-1] != ' ' and self.__analyserSettings.getShiftStateAndClear():
            self.__finalList[-1] = self.__finalList[-1].capitalize()

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
    
    def _processWord(self, word):
        if word == self.__explicit:
            self.__analyserSettings.setExplicit()
        elif word == self.__switchShift:
            self.__analyserSettings.setShift()
        else:
            if word in settings['keyboard_mapping'].keys():
                self.__finalList.append(settings['keyboard_mapping'][word])
            else:
                self.__finalList.append(word)
            

    def process(self, text):
        for word in text.split():
            if self.__analyserSettings.getExplicit():
                self._processWordAsExplicit(word)
            else:
                self._processWord(word)

            if len(self.__finalList) > 0 and not self.__analyserSettings.checkExplicit() and word != self.__switchShift:
                self._appendCapitalIfNeeded()
                self._appendSpaceIfNeeded()
            
        self._deleteSpacesIfNeeded()

        return self.__finalList

if __name__ == "__main__":
    pass