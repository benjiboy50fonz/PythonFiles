import sys
import weakref
from random import randint

from .inventorycontrol import InventoryControl

sys.path.insert(1, '/home/benji/Git/PythonFiles/PythonFiles/TextAdventureEngine') # Allows an import of the custom error and room stuff.

from customerrors import CustomErrors

from inputtranslations import InputTranslations

class LootRoom(CustomErrors):
    
    inventoryControl = InventoryControl()
    inptrans = InputTranslations()
    
    def __init__(self, name, location, textWhenFound, quantity=1, addToInventory_=True, chanceOfReceiving=1, lootOnEnter=False): # Chance of receiving should be a 1 out of this integer.
        
        super().__init__()
                
        self.name = name 
        self.quantity = quantity
        
        #if not isinstance(location, Room):
            #raise self.INVALIDROOMGIVEN('Please provide a object of the Room class for the location argument!')
        
        self.textWhenFound = textWhenFound
        self.location = location
        
        self.addToInventory_ = addToInventory_
        self.chanceOfReceiving = chanceOfReceiving
        self.lootOnEnter = lootOnEnter
        
        self.roomAddToContaining()
        
    def findItem(self):
        fp(self.textWhenFound)
        
        fail = True
        
        while fail:
            res = fi('Would you like to take it?')
            if res in self.inptrans.yes:
                self.addToInventory()
            elif res in self.inptrans.no:
                pass
            else:
                continue
            
            fail = False
            
    def displayInventory(self):
        self.inventoryControl.displayInventory()
            
    def addToInventory(self):
        if self.addToInventory_:
            if randint(1, self.chanceOfReceiving) == 1:
                self.inventoryControl.appendObject(self.name, self.quantity)
                
    def roomAddToContaining(self):
        self.location.containing.add(weakref.ref(self))
        
    def setGlobalInventorySpace(self, num):
        '''
        This thicc boi is spedecial. Unlike the others here, it is only necessary to call this once because it modifies the global InventoryControl.
        '''
        if self.inventoryControl.setMaxCapacity(num):
            fp('Success!')
        else:
            fp('Could not set storage limit because the inventory stock would exceed it! Try seting this at the beginning instead!')
        
        
def fp(text):
    print('\n' + str(text))
    
def fi(text):
    res = str(input('\n' + str(text) + ':')).lower()
    return res
