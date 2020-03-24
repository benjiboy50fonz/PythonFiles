import sys

sys.path.insert(1, '/home/benji/Git/PythonFiles/PythonFiles/TextAdventureEngine') # Allows an import of the custom error stuff.

from customerrors import CustomErrors

class InventoryControl(CustomErrors):
    
    def __init__(self, sizeLimit=None):
        
        '''
        This will control the character's inventory. Add things like weapons, maps, or food here. 
        '''
        
        super().__init__()
        
        self.vacantSpace = sizeLimit
        
        if sizeLimit != None: 
            self.maxCapacity = int(sizeLimit)
            self.vacantSpace = self.maxCapacity
            
        self.inventory = {}    
        
    def appendObject(self, name, quantity=1):
        try:
            if quantity > self.vacantSpace: # Gets the remaining space that is vacant. 
                quantity = self.vacantSpace # Says that you can only pickup and the max amount, and only allows that much. 
                self.vacantSpace = 0 
                
            self.findAndAdd(name, quantity)
            
        except(TypeError): # There must be infinite space, so ignore the limit.
            self.findAndAdd(name, quantity)
            
    def findAndAdd(self, name, quantity):
        if name in self.inventory.keys():
            self.inventory[name] += quantity
        else:
            self.inventory[name] = quantity
            
        fp('Successfully added!')
            
        self.updateVacancy()
            
    def updateVacancy(self):
        try:
            self.vacantSpace = self.maxCapacity - sum(self.inventory.values())
        
            if self.vacantSpace < 0:
                raise self.YOUBROKETHEINVENTORY('You somehow have more than the allowed number of items. Backend, investigate!')
            
        except(AttributeError):
            pass
                                   
    def removeObject(self, name, quantity=1):
        if name in self.inventory.keys():
            self.inventory.pop(name)
        else:
            fp('You don\' have of that in your inventory!')
        
        self.updateVacancy()
        
    def displayInventory(self):
        self.updateVacancy()
        
        try: 
            print('------------------------')
            print('Max Capacity: ' + str(self.maxCapacity))
            print('Vacant Spots: ' + str(self.vacantSpace))
            for set_ in self.inventory.items():
                print('Name ' + str(set_[0]) + ' Quantity: ' + str(set_[1]))
            print('------------------------')
            
        except(AttributeError):
            print('Max Capacity: No limit.')
            print('Vacant Spots: No limit.')
            if len(self.inventory.keys()) == 0:
                print('Your Inventory is Empty!')
            else:
                for set_ in self.inventory.items():
                    print('Name ' + str(set_[0]) + ' Quantity: ' + str(set_[1]))
            print('------------------------')
            
    def clearDictionary(self):
        self.inventory.clear()
        
    def setMaxCapacity(self, num):
        if sum(self.inventory.values()) > num:
            return False
            
        self.maxCapacity = num
        return True

def fp(text):
    print('\n' + str(text))
