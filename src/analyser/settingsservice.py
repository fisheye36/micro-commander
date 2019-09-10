from conf import settings
import analyser.insertservice
import analyser.analyserhelper as Helper
import logger

class SettingsService:
    def __init__(self, analyserSettings):
        logger.info('Entering dedicated Settings Service')
        self.__analyserSettings = analyserSettings
        self.__finalList = []

    def _processAsAnalyserSettings(self, listOfWords):
        if not Helper.checkIfAllListElementsAreStrings(listOfWords):
            logger.info('Unexpected input')    
            return
        command = ' '.join(listOfWords).lower()
        if command == settings['analysersettings']['autospace']:
            self.__analyserSettings.switchAutoSpace()
            return
        elif command == settings['analysersettings']['micOn']:
            self.__analyserSettings.turnOnMic()
            return
        elif command == settings['analysersettings']['micOff']:
            self.__analyserSettings.turnOffMic()
            return

        logger.info('No setting found for: {}'.format(command))    

    def process(self, text):
        listOfWords = text.split()
        del listOfWords[0]
        self._processAsAnalyserSettings(listOfWords)
        return self.__finalList

if __name__ == "__main__":
    pass