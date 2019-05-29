from conf import settings
from enum import Enum
from copy import deepcopy

STATE = {
    'NORMAL' : 0,
    'EXACT' : 1
}

class Analyser:
    def __init__(self):
        self.state = STATE['NORMAL']
        self.finalList = []

    def analyse(self, text):
        text = text.split()
        for word in text:
            if self.state == STATE['NORMAL']:
                self.normalStateProcess(word)        
            elif self.state == STATE['EXACT']:
                self.exactStateProcess(word)

    def normalStateProcess(self, word):
        magicWords = settings['magicWords']
        if word in magicWords:
            self.state = magicWords[word]
            break
        else:
            self.finalList.append(word)

    def exactStateProcess(self, word):
        self.finalList.append(word)
        self.state = STATE['NORMAL']

    def reset(self):
        self.finalList = []
        self.state = STATE['NORMAL']

    def getFinalCommand(self):
        toReturn = deepcopy(self.finalList)
        self.reset()
        return toReturn


if __name__ == "__main__":
    pass
