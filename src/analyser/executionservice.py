from conf import settings
from analyser.insertservice import InsertService
import subprocess
import logger

class ExecutionService(InsertService):
    def __init__(self, analyserSettings):
        InsertService.__init__(self, analyserSettings)
        self.__finalList = []

    def _execute(self, words):
        words = [x for x in words if x != ' ']

        dic = settings['execute']
        for key in dic:
            if set(key.split()) <= set(words):
                lenOfKeyElements = len(key.split())
                del words[:lenOfKeyElements]
                try:
                    print(words)
                    words.insert(0, dic[key])
                    print(words)
                    subprocess.run(words)
                except:
                    logger.info('Something went wrong when trying to execute command')

    def process(self, text):
        listOfWords = text.split()
        del listOfWords[0]
        words = super().process(' '.join(listOfWords))

        if not self._checkIfAllListElementsAreStrings(words):
            logger.info('Something went wrong')
            return []
        
        self._execute(words)

        return []
        

if __name__ == "__main__":
    pass