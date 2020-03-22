import sys
import weakref
from random import randint

from inventorycontrol import InventoryControl

sys.path.insert(1, '/home/benji/Git/PythonFiles/PythonFiles/TextAdventureEngine') # Allows an import of the custom error and room stuff.

from customerrors import CustomErrors

from room import Room

class LootRoom(CustomErrors):
    
    inventoryControl = InventoryControl()
    
    def __init__(self, name, location, textWhenFound, quantity=1, addToInventory=True, chanceOfReceiving=1): # Chance of receiving should be a 1 out of this integer.
        
        super().__init__()
                
        self.name = name 
        self.quantity = quantity
        
        if not isinstance(location, Room):
            raise self.INVALIDROOMGIVEN('Please provide a object of the Room class for the location argument!')
        
        self.location = location
        
        self.addToInventory = addToInventory
        self.chanceOfReceiving = chanceOfReceiving
        
        self.roomAddToContaining()
        
    def findItem(self):
        fp(self.textWhenFound)
        self.addToInventory()
        
    def addToInventory(self):
        if self.addToInventory:
            if randint(1, self.chanceOfReceiving) == 1:
                self.inventoryControl.appendObject(self.name, self.quantity)
                
    def roomAddToContaining(self):
        self.location.containing.append(weakref.ref(self))
        
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
