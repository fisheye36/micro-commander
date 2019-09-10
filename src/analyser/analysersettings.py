import logger

class AnalyserSettings:
    def __init__(self):
        self.__isExplicit = False
        self.__autoSpace = True
        self.__isMicOn = True
    
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
        if self.__autoSpace == True:
            logger.info('AutoSpace - ON')
        else:
            logger.info('AutoSpace - OFF')
    
    def turnOnMic(self):
        logger.info('Microphone - ON')
        self.__isMicOn = True

    def turnOffMic(self):
        logger.info('Microphone - OFF')
        self.__isMicOn = False
    
    def getMicState(self):
        return self.__isMicOn


    
