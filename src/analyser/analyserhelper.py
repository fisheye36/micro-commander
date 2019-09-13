from collections import Counter

def checkIfAllListElementsAreStrings(listOfWords):
    for el in listOfWords:
        if not isinstance(el, str):
            return False
    return True

def sublist(lst1, lst2):
    c1 = Counter(lst1)
    c2 = Counter(lst2)
    for item, count in c1.items():
        if count > c2[item]:
            return False
    return True
