from analyser.capitalletters import CapitalLetters
import logger

class AnalyserSettings:
    def __init__(self):
        self.__isExplicit = False
        self.__autoSpace = True
        self.__isMicOn = True
        self.__shift = False
        self.__capitalLetters = CapitalLetters.AUTO

    def setShift(self):
        self.__shift = True

    def setCapitalLettersState(self, state):
        print("Capital letters set to: ", state)
        self.__capitalLetters = state

    def getCapitalLettersState(self):
        return self.__capitalLetters

    def getShiftStateAndClear(self):
        val = self.__shift
        self.__shift = False
        return val

    def setExplicit(self):
        self.__isExplicit = True

    def checkExplicit(self):
        return self.__isExplicit

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


    
