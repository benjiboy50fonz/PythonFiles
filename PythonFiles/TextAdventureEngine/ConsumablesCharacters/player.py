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
            
            count = 0
            for item in list(currentWeapons.items()):
                count += 1
                try:
                    print(str(count) + '. ' + str(item[0][0]).upper() + str(item[0][1:]).lower() + '   Damage: ' + str(item[1][2]))
                
                except(IndexError):
                    continue
                
                
            print(str(count + 1) + '. Fists   Damage: ' + str(self.fistDamage))
            
            wrong = True
                
            while wrong:
                selection = fi(':')
            
                try:
                    selectedWeaponData = list(currentWeapons.values())[int(selection) - 1]
                    wrong = False
                    
                except(TypeError, IndexError):
                    fp('Enter a valid value!')
                    continue
                        
        elif range_ is True:
            count = 0
            closeWeapons = {}
            
            for item in currentWeapons.items():
                if item[1][1] is True:
                    closeWeapons[item[0]] = item[1]
            
            for item in list(closeWeapons.items()):
                count += 1
                try:
                    print(str(count) + '. ' + str(item[0][0]).upper() + str(item[0][1:]).lower() + '   Damage: ' + str(item[1][2]))
                
                except(IndexError):
                    continue
                
                
            print(str(count + 1) + '. Fists   Damage: ' + str(self.fistDamage))
            
            wrong = True
                
            while wrong:
                selection = fi(':')
            
                try:
                    selectedWeaponData = list(closeWeapons.values())[int(selection) - 1]
                    wrong = False
                    
                except(TypeError, IndexError):
                    fp('Enter a valid value!')
                    continue
            
            
        elif range_ is False:
            count = 0
            farWeapons = {}
            
            for item in currentWeapons.items():
                if item[1][1] is False:
                    farWeapons[item[0]] = item[1]
            
            for item in list(farWeapons.items()):
                count += 1
                try:
                    print(str(count) + '. ' + str(item[0][0]).upper() + str(item[0][1:]).lower() + '   Damage: ' + str(item[1][2]))
                
                except(IndexError):
                    continue
                
                
            print(str(count + 1) + '. Fists   Damage: ' + str(self.fistDamage))
            
            wrong = True
                
            while wrong:
                selection = fi('')
            
                try:
                    selectedWeaponData = list(farWeapons.values())[int(selection) - 1]
                    wrong = False
                    
                except(TypeError, IndexError):
                    fp('Enter a valid value!')
                    continue
                
        else:
            raise self.INVALIDWEAPONRANGEPROVIDED('Please provide a bool or None for the range_ argument.')
                
        return selectedWeaponData
                
    def beginFight(self, playerAttacksFirst, applicableRange=None):
        
        '''
        The fighting sequence will begin here for the player.
        '''
        
        self.selectWeapon(applicableRange)
    
    def useGadget(self):
        pass
    
    def focusOnEnemy(self, enemies):
        count = 0
        for enemy in enemies:
            count += 1
            print(str(count) + '. ' + str(enemy.id_[0]).upper() + str(enemy.id_[1:]).lower() + '   Damage: ' + str(enemy.d) + '   Health: ' + str(enemy.health))
            
        res = fi('')
        enemy = enemies[res - 1]
    
        return enemy
        
    def destroyWeaponAfterUse(self):
        pass
    
    def useAmmo(self, quantity=1):
        pass

def fp(text):
    print('\n' + str(text))

def fi(text):
    res = str(input('\n' + str(text) + ':')).lower()
    return res
