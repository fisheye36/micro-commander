def checkIfAllListElementsAreStrings(listOfWords):
    for el in listOfWords:
        if not isinstance(el, str):
            return False
    return True
