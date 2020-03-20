from customerrors import CustomErrors

class Room(CustomErrors):
    
    def __init__(self, name, dirString, entryText, printOnEnter=True):
        
        super().__init__()
        
        self.name = name
        self.dirString = dirString
        self.entryText = entryText
        self.printOnEnter = printOnEnter

        self.printWhenEntered(self.printOnEnter)
        
    def printWhenEntered(self, printImmediately):
        if printImmediately:
            fp(self.entryText)
            
    def lootRoom(self):
        pass

    def fightInRoom(self):
        pass
    
    def customAction(self):
        pass

def fp(text):
    print('\n' + str(text))
