from conf import settings
from pynput.keyboard import Key
import logger
from analyser.insertservice import InsertService

class BackspaceService(InsertService):
    def __init__(self, analyserSettings):
        logger.info('Entering dedicated Backspace Service')
        self.__finalList = []
        self.__deleteAll = settings['analysersettings']['deleteAll']

    def process(self, text):
        listOfWords = text.split()
        if len(listOfWords) == 1:
            logger.info('Deleting one character')
            self.__finalList.append(Key.backspace)
        elif len(listOfWords) == 2:
            try:
                nOfBackspaces = int(listOfWords[1])
                logger.info('Deleting {} characters'.format(nOfBackspaces))
                self.__finalList = [Key.backspace] * nOfBackspaces
            except:
                if listOfWords[1].lower() == self.__deleteAll:
                    logger.info('Deleting all characters')
                    self.__finalList = [(Key.ctrl_l, 'a'), Key.backspace]
                else:
                    logger.info('Invalid arguments passed to BackspaceService')
        else:
            logger.info('Too many arguments for BackspaceService')
        return self.__finalList

if __name__ == "__main__":
    pass