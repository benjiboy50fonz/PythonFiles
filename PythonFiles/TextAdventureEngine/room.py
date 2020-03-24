from customerrors import CustomErrors

from ConsumablesCharacters.lootroom import LootRoom

class Room(CustomErrors):

    def __init__(self, name, dirString, entryText, availableActions: str='', fightFirst=True, enemies=[], enableActOnEnter=True, actionText='', printOnEnter=True): 
        
        # It's important to include the correct characters in the availableActions string. THE ORDER OF EVENTS WILL FOLLOW THE STRING'S ORDER (fightFirst is the exception)!
        
        super().__init__()
        
        self.containing = set([])
        self.enemies = enemies
        
        self.looted = False
        
        self.stringToAction = {'l' : 'self.lootRoom(char)',
                               'f' : 'self.fightInRoom(char)',
                               'c' : 'self.customAction(char)',
                               'o' : 'self.offerFlee(char)'
                                }
        
        self.availableActions = availableActions
        self.fightFirst = fightFirst
        self.enableActOnEnter = enableActOnEnter
        self.actionText = actionText
        self.name = name
        self.dirString = dirString
        self.entryText = entryText
        self.printOnEnter = printOnEnter
                
        self.multipleTexts = False
        
        if type(self.actionText) is dict:
            self.multipleTexts = True
        
        for enemy in self.enemies:
            fp(enemy.healthWithArmor) 
        
    def printWhenEntered(self, printImmediately):
        if printImmediately:
            fp(self.entryText)
            
    def enterRoom(self):
        self.printWhenEntered(self.printOnEnter)
            
        if self.fightFirst and ('f' in self.availableActions): # Fight first if needed.
            self.initiateAction('f')
            
        if len(self.containing) != 0 and not self.looted:
            for lootable in self.getinstances(): # Loot first if loot on enter is enabled.
                if lootable.lootOnEnter:
                    lootable.findItem()
            
        if self.enableActOnEnter:
            for char in self.availableActions:
                self.initiateAction(char)
            
    def initiateAction(self, char):
        try:
            eval(self.stringToAction[char])
        except(KeyError):
            pass
        
    def printTexts(self, printOne=''):
        if self.multipleTexts:
            fp(self.actionText[printOne])
        else:
            fp(self.actionText)
        
    def lootRoom(self, char):
        if not self.looted:
            self.printTexts(char)
            
            for lootable in self.getinstances():
                lootable.findItem()
        
        
    def fightInRoom(self, char):
        self.printTexts(char)

        fp('Fighting now!')
    
    def offerFlee(self, char):
        self.printTexts(char)

        fp('Fleeing now!')
    
    def customAction(self, char):
        self.printTexts(char)

        fp('Custom boi started')
        
    def leaveRoom(self):
        pass
    
    def getinstances(self):
        dead = set()
        for ref in self.containing:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        self.containing -= dead
        
def fp(text):
    print('\n' + str(text))
