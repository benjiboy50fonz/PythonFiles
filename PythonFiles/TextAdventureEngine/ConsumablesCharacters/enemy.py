import sys
import random

sys.path.insert(1, '/home/benji/Git/PythonFiles/PythonFiles/TextAdventureEngine') # Allows an import of the custom error and room stuff.

from customerrors import CustomErrors

class EnemyType(CustomErrors):
    
    '''
    When using enemy mechanics, call individual commands by calling upon renamed, general commands. 
    '''
    
    d = 0
    counter = None
    attack = None
    
    globalDefaultHealth = 5
    globalDefaultSkillLevel = 0.4
    globalDefaultPointsPerKill = 10
    
    enemyTypes = {'ene' : []}
    
    def __init__(self, id_, healthWithArmor='def', damageWithClose=None, damageWithFar=None, skillLevel='def', pointsPerKill='def', accessClass=False):
        
        '''
        Skill level is a singleton that is pretty much used to determine the survivability and skill of the enemy.
        It should be given a value between 0 and 100, 100 being more skilled (even though the toughest enemy will only have a max chance of 80%!; use boss class if you'd like higher!
        '''
        
        super().__init__()

        if not accessClass:
            
            self.enemyTypes[id_] = [healthWithArmor, damageWithClose, damageWithFar, skillLevel, pointsPerKill]
            
            self.hidden = False
            
            self.damageWithClose = damageWithClose
            self.damageWithFar = damageWithFar
                
            if skillLevel == 'def':
                self.skillLevel = self.globalDefaultSkillLevel
            else:
                if skillLevel > 100.0 or skillLevel < 0.0:
                    raise self.SKILLLEVELNOTPOSSIBLE('Please provide a skill level between 0 and 1, 1 being more skilled.')
                
                self.skillLevel = float(skillLevel / 100) # Makes it a float, a type easier for us to use.
            
            if healthWithArmor == 'def':
                self.health = self.globalDefaultHealth
            else:
                self.health = healthWithArmor
                
            if pointsPerKill == 'def':
                self.pointsPerKill = self.globalDefaultPointsPerKill
            else:
                self.pointsPerKill = pointsPerKill
            
            if damageWithClose != None and type(damageWithClose) == int and damageWithFar == None:
                self.setupCloseEnemy()
                
            elif damageWithFar != None and type(damageWithFar) == int and damageWithClose == None:
                self.setupFarEnemy()
            
            elif type(damageWithFar) == int and type(damageWithClose) == int:
                self.setupVersatileEnemy()
        
            else:
                raise self.INVALIDSTRINGGIVEN('Please provide the damage for the close or far, depending on which you\'d like, or both for a very versatile enemy!')
            
            self.sl = self.assignActualChances()
        
    def getListOfEnemies(self):
        return self.enemyTypes
        
    def assignActualChances(self):
        return self.skillLevel / 0.8
    
    def setDefaultLevel(self, level):
        self.globalDefaultLevel = level
        
    def setDefaultHealth(self, health):
        self.globalDefaultHealth = health
        
    def setDefaultSkillLevel(self, level):
        if level > 1.0 or level < 0.0:
                raise self.SKILLLEVELNOTPOSSIBLE('Please provide a skill level between 0 and 1, 1 being more skilled.')
        else:
            self.globalDefaultSkillLevel = level
        
    def setDefaultPointsPerKill(self, points):
        self.globalDefaultPointsPerKill = points
        
    def setupCloseEnemy(self):
        self.counter = self.counterClose
        self.attack = self.attackClose
        self.d = self.damageWithClose
    
    def setupFarEnemy(self):
        self.counter = self.counterFar
        self.attack = self.attackFar
        self.d = self.damageWithFar
    
    def setupVersatileEnemy(self):
        self.counter = self.counterWithDistance
        self.attack = self.attackWithType
        
    def blockAny(self, distance):            
        if not type(distance) == str:
            raise self.INVALIDSTRINGGIVEN('Please provide a string and declare the attack type, ranged or near!')
    
    def flee(self, fleePossible=True):
        if self.odds(-0.1) and fleePossible: # Gives an extra 10% of failure  
            return True, 3
        return False, 0
    
    def counterFar(self, dist=None):
        if self.odds(-0.05):
            damage = self.d * random.uniform(0.4, 0.7)
            return True, damage
        return False, 0
    
    def counterClose(self, dist=None):
        if self.odds():
            damage = self.d * random.uniform(0.35, 0.65)
            return True, damage
        return False, 0
    
    def counterWithDistance(self, dist):
        if dist == 'far':
            if self.odds(-0.05):
                damage = self.d * random.uniform(0.4, 0.7)
                return True, damage
            return False, 0
    
        elif dist == 'close': 
            if self.odds():
                damage = self.d * random.uniform(0.35, 0.65)
                return True, damage
            return False, 0
        
        else:
            raise self.INVALIDSTRINGGIVEN('Please provide dist with \'close\' or \'far\'!')
        
    def attackFar(self, style=None): # A ranged attack, harder to counter but easier for the enemy to miss.
        if self.odds(-0.15): # Lower chance because they can miss, not too high tho because the player can counter!
            final = abs(self.d + random.randint(-5, 5))
            return True, final
        return False, 0
    
    def attackClose(self, style=None): # A melee attack of some sort which involves the enemy probably suceeding, but a more availble player counter. 
        if self.odds(-0.05): # Lower chance because they can miss, not too high tho because the player can counter!
            final = abs(self.d + random.randint(-3, 3))
            return True, final
        return False, 0
    
    def attackWithType(self, style): # Used in instances where the enemy can attack both close and far
        if style == 'far':
            if self.odds(-0.15): # Lower chance because they can miss, not too high tho because the player can counter!
                final = abs(self.d + random.randint(-5, 5))
                return True, final
            return False, 0
        
        elif style == 'close':
            if self.odds(-0.05): # Lower chance because they can miss, not too high tho because the player can counter!
                final = abs(self.d + random.randint(-3, 3))
                return True, final
            return False, 0
    
        else:
            raise self.INVALIDSTRINGGIVEN('Please provide style with \'close\' or \'far\'!')
    
    def odds(self, boost=0):
        if random.random() <= self.sl + boost:
            return True # True because the action was successful
        return False

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return False, self.pointsPerKill # False because he is dead 
        else:
            return True, None # True because he can continue attacking
    
    def dieAndDrop(self, provideLoot=None):
        if type(provideLoot) == str:
            return provideLoot
        # Call this in the engine die function, then actually kill the object.
        

        
            
            
