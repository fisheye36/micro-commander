from conf import settings
from copy import deepcopy

class Analyser:
    def __init__(self):
        self.finalList = []

    def analyse(self, text):
        # TODO implement analysis mechanism and remove below temporary solution
        self.finalList = text.split()
        return self.finalList

if __name__ == "__main__":
    pass