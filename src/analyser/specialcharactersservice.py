from conf import settings
from analyser.insertservice import InsertService
import logger

class SpecialCharactersService(InsertService):
    def __init__(self, analyserSettings):
        InsertService.__init__(self, analyserSettings)
        logger.info('Entering dedicated Special Characters Service')
        self.__analyserSettings = analyserSettings
        self.__finalList = []

    def _processAsSpecialCharacter(self, words):
        key = ' '.join(words)
        if key in settings['keyboard_mapping'].keys():
            self.__finalList.append(settings['keyboard_mapping'][key])
            return
        
        logger.info('No special character found for: {}'.format(key))
        
    def process(self, text):
        listOfWords = text.split()
        del listOfWords[0]
        listOfWords = [word.lower() for word in listOfWords]
        self._processAsSpecialCharacter(listOfWords)
        return self.__finalList

if __name__ == "__main__":
    pass