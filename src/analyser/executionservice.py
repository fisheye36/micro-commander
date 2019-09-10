from conf import settings
from analyser.insertservice import InsertService
import analyser.analyserhelper as Helper
import subprocess
import logger

class ExecutionService(InsertService):
    def __init__(self, analyserSettings):
        InsertService.__init__(self, analyserSettings)
        logger.info('Entering dedicated Execution Service')
        self.__finalList = []

    def _execute(self, words):
        words = [word for word in words if word != ' ']

        dic = settings['execute']
        for key in dic:
            if set(key.split()) <= set(words):
                lenOfKeyElements = len(key.split())
                del words[:lenOfKeyElements]
                try:
                    words.insert(0, dic[key])
                    subprocess.run(words)
                except:
                    logger.info('Something went wrong when trying to execute command')

    def process(self, text):
        listOfWords = text.split()
        del listOfWords[0]
        words = super().process(' '.join(listOfWords))

        if not Helper.checkIfAllListElementsAreStrings(words):
            logger.info('Unexpected input')
        else:
            self._execute(words)

        return self.__finalList
        

if __name__ == "__main__":
    pass