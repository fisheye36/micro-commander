from conf import settings

class InsertService:
    def __init__(self, analyser):
        self.name = "INSERT"
        self.analyser = analyser
        self.explicit = 'dosłownie' #settings.data['general']['key_words']['explicit'] - TODO COS NIE BANGLA 
        self.is_explicit = False
        self.finalList = []

    def process(self, text):
        self.list = text.split()

        for word in self.list:
            if word == self.explicit and self.is_explicit == False:
                self.is_explicit = True
            else:
                if self.is_explicit == True:
                    self.finalList.append(word)
                    self.is_explicit = False
                else:
                    if word in settings['keyboard_mapping'].keys():
                        self.finalList.append(settings['keyboard_mapping'][word])
                    else:
                        self.finalList.append(word)
                self.finalList.append(' ')

        if len(self.finalList) > 0:
            del self.finalList[-1]
        return self.finalList

if __name__ == "__main__":
    pass