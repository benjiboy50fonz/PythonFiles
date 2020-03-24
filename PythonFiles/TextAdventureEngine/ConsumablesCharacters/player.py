import sys

from .inventorycontrol import InventoryControl

sys.path.insert(1, '/home/benji/Git/PythonFiles/PythonFiles/TextAdventureEngine') # Allows an import of the custom error and room stuff.

from customerrors import CustomErrors

class Player(CustomErrors):
    
    '''
    Includes the players actions and statistics, but not the story line! The fist damage will be used if the player has no other weapons.
    '''
        
    def __init__(self, startHealth=30, fistDamage=3, inventoryCapacity=None):
    
        super().__init__()

        self.health = startHealth
        self.fistDamage = fistDamage
        
        self.inventoryControl = InventoryControl(inventoryCapacity)
        
    def selectWeapon(self, range_=None):
        currentWeapons = {}
        for item in (self.inventoryControl.getInventory()).items():
            if item[1][1] is not None:
                currentWeapons[item[0]] = item[1]
           
        fp('Please enter the number of the weapon you\'d like to fight with!')
        
        if range_ is None:
            
            count = 1
            for item in currentWeapons:
                print(str(count) + '. ' + str(item[0]) + '   Damage: ' + str(item[1][2]))
                count += 1
                
            print(str(count) + '. Fists   Damage: ' + str(self.fistDamage))
                      
            
    def beginFight(self, playerAttacksFirst):
        pass

def fp(text):
    print('\n' + str(text))

def fi(text):
    res = str(input('\n' + str(text) + ':')).lower()
    return res
