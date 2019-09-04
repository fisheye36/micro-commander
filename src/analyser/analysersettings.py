class AnalyserSettings:
    def __init__(self):
        self.__isExplicit = False
        self.__autoSpace = True
    
    def setExplicit(self):
        self.__isExplicit = True

    def getExplicit(self):
        if self.__isExplicit == True:
            self.__isExplicit = False
            return True
        return False

    def getAutoSpace(self):
        return self.__autoSpace

    def switchAutoSpace(self):
        self.__autoSpace = not self.__autoSpace

    
