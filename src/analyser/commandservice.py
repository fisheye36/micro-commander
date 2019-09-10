from conf import settings
from analyser.insertservice import InsertService
import logger

class CommandService(InsertService):
    def __init__(self, analyserSettings):
        InsertService.__init__(self, analyserSettings)
        logger.info('Entering dedicated Command Service')
        self.__analyserSettings = analyserSettings
        self.__finalList = []

    def _processAsCommand(self, words):
        command = ''.join(words)
        if command in settings.active()['commands'].keys():
            self.__finalList = settings.active()['commands'][command]
            return
        logger.info('No command found for: {}'.format(command))    
        return

    def process(self, text):
        listOfWords = text.split()
        del listOfWords[0]
        words = super().process(' '.join(listOfWords))        
        self._processAsCommand(words)
        return self.__finalList

if __name__ == "__main__":
    pass