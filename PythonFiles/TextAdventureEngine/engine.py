#!/usr/bin/env python3

from customerrors import CustomErrors

from room import Room
from roomcluster import RoomCluster

from ConsumablesCharacters.enemy import EnemyType
from ConsumablesCharacters.newenemy import NewEnemy
from ConsumablesCharacters.player import Player

from ConsumablesCharacters.lootroom import LootRoom
from ConsumablesCharacters.inventorycontrol import InventoryControl

class TextAdventureGameEngine(CustomErrors):
    
    '''
    Key, universal terms for directions:
    Left: 'l'
    Right: 'r'
    Forward: 'f'
    Back: 'b'
    Unknown: '!'
    '''
    
    inventoryManager = InventoryControl()
    
    player = Player()
                
    def __init__(self, startRoom, startMap, searchables=[], allowBack=True, defaultDirections=None):
        super().__init__()
            
        self.points = 0
            
        self.startRoom = startRoom
        self.startMap = startMap
        
        self.lastMove = ''
        
        self.moveRelations = {'right' : 'r',
                              'left' : 'l',
                              'forward' : 'f',
                              'back' : 'b'
                             }
        
        if not isinstance(self.startRoom, Room):
            raise self.INVALIDOBJECT('Please pass an object of the Room class!')
        
        self.currentRoom = self.startRoom.name
        self.currentRoomObj = self.startRoom
        
        self.currentMap = self.startMap
        
        if not isinstance(self.startMap, RoomCluster):
            raise self.INVALIDOBJECT('Please pass an object of the RoomCluster class!')
        
        for row in self.startMap.map_:
            try:
                self.currentX = row.index(self.startRoom) # Finds the x position by looking at each row in self.startMap, and trying to find the self.startRoom. 
                self.currentY = self.startMap.map_.index(row) # Finds the y position by looking for the specific row in the self.startMap. 
                break
            
            except(ValueError):
                pass
        
        print(self.getAndUpdateIndexes(self.startMap, self.startRoom))
        
        self.searchables = searchables
        self.allowBack = allowBack
        self.globalUnknown = '!'
        self.globalKnowns = ['l', 'r', 'f', 'b']
                
        self.movesMade = 0
    
        self.defaultDirections = self.generateDirections()
        self.cardinalDirections = self.generateCardinalDirections()
        
        if type(defaultDirections) == dict:
            self.defaultDirections = defaultDirections # Updates the directions that are available with the given, custom directions.
            
    def getAndUpdateIndexes(self, map__, room):
        mapp = map__.map_ # Ew, gross. But this basically takes the cluster object, takes its map attribute and makes it a variable. Don't be afraid!
        
        for row in mapp:
            try:
                self.currentX = row.index(room) # Finds the x position by looking at each row in self.startMap, and trying to find the self.startRoom. 
                self.currentY = mapp.index(row) # Finds the y position by looking for the specific row in the self.startMap. 
                break
            except(ValueError):
                pass
        
        return self.currentX, self.currentY
        
    def generateDirections(self, f='f', l='l', r='r', b='b'):
        
        return {
            'forward' : f,
            'straight' : f,
            'onward' : f,
            'right' : r,
            'left' : l, 
            'back' : b, 
            'reverse' : b
            }
            
    def generateCardinalDirections(self):
        # Lol working on it
        return {}
    
    def interpretDirection(self, entry):
        # Strip and normalize the entry
        normalizedEntry = (str(entry).strip()).lower()
    
        try:
            return self.defaultDirections[normalizedEntry]
        
        except(KeyError): # If it is not in the default directions, check the cardinal.
            try:
                return self.cardinalDirections[normalizedEntry]
                
            except(KeyError):
                return self.globalUnknown # If it is not in the cardinal either, return the universal unknown.
        
        
    def move(self, rawEntry):
        # Check for valid directions
        
        directions = self.currentRoomObj.dirString
        
        for char in str(directions.lower()).strip():
            if char not in self.globalKnowns:
                raise self.INVALIDDIRECTIONSTRING('Invalid character in string. Please refer to the global characters.') # Raise a custom, invalid direction string error
            
        normalizedEntry = self.interpretDirection(rawEntry)
        
        if normalizedEntry is self.globalUnknown:
            return 2
        
        elif (normalizedEntry not in directions):
            return 3
        
        elif normalizedEntry in directions:
            res, newRoom = self.moveIfPossible(normalizedEntry)
            if res and (newRoom is not None and newRoom is not False): # checks for a successful exit and a non-pseudo newRoom object.
                self.movesMade += 1
                newRoom.enterRoom()
                
        
    def moveIfPossible(self, entry, move=True):
        
        entryToMethod = {'f' : 'forward',
                         'l' : 'left', 
                         'r' : 'right',
                         'b' : 'back'
                             }
        
        # Interpret the entry so we can use it with the previous move. 
        
        newMove = entryToMethod[entry]
        
        # Determine directions based off of which way we're facing. 
        
        if self.lastMove == 'l':
            
            
            self.moveRelations = {'right' : 'f',
                                  'left' : 'b',
                                  'forward' : 'l',
                                  'back' : 'b'
                                 }
            
        elif self.lastMove == 'r':
            
            self.moveRelations = {'right' : 'b',
                                  'left' : 'f',
                                  'forward' : 'r',
                                  'back' : 'l'
                                 }
            
        elif self.lastMove == 'b':
            
            self.moveRelations = {'right' : 'l',
                                  'left' : 'r',
                                  'forward' : 'b',
                                  'back' : 'f'
                                 }
            
        else:
            self.moveRelations = {'right' : 'r',
                                  'left' : 'l',
                                  'forward' : 'f',
                                  'back' : 'b'
                                 }
            
        realDirection = self.moveRelations[newMove]
        
        
        x, y = self.getAndUpdateIndexes(self.currentMap, self.currentRoomObj) # Remember, currentMap is actually an object! Call the property map_!

        if realDirection == 'l':
            
            try: 
                
                possible = (self.currentMap.map_[y][x - 1]).name
                if not move:
                    return True # If you just wanted to see if it's possible, end now!
                self.currentRoom = (self.currentMap.map_[y][x - 1]).name
                self.currentRoomObj = (self.currentMap.map_[y][x - 1])
                
                newX, newY = self.getAndUpdateIndexes(self.currentMap, self.currentRoomObj)
                
            except(KeyError):
                return False
        
        elif realDirection == 'r':
            
            try: 
                
                possible = (self.currentMap.map_[y][x + 1]).name
                if not move:
                    return True # If you just wanted to see if it's possible, end now!
                self.currentRoom = (self.currentMap.map_[y][x + 1]).name
                self.currentRoomObj = (self.currentMap.map_[y][x + 1])
                
                newX, newY = self.getAndUpdateIndexes(self.currentMap, self.currentRoomObj)
                
            except(KeyError):
                return False
                
        elif realDirection == 'b':
            
            try: 
                
                possible = (self.currentMap.map_[y + 1][x]).name
                if not move:
                    return True # If you just wanted to see if it's possible, end now!
                self.currentRoom = (self.currentMap.map_[y + 1][x]).name
                self.currentRoomObj = (self.currentMap.map_[y + 1][x])
                
                newX, newY = self.getAndUpdateIndexes(self.currentMap, self.currentRoomObj)
                
            except(KeyError):
                return False
            
        elif realDirection == 'f':
                
            try: 
                
                possible = (self.currentMap.map_[y - 1][x]).name
                if not move:
                    return True # If you just wanted to see if it's possible, end now!
                self.currentRoom = (self.currentMap.map_[y - 1][x]).name
                self.currentRoomObj = (self.currentMap.map_[y - 1][x])
                
                newX, newY = self.getAndUpdateIndexes(self.currentMap, self.currentRoomObj)                
            
            except(KeyError):
                return False
            
        # Updates the last move after a successful move. 
            
        self.lastMove = realDirection
        
        return True, (self.currentMap.map_[newY][newX]) # returns true because it was successful and the new room object
        
    def fight(self, enemies: list, range_=None, playerAttacksFirst=True):
        
        for enemy in enemies:
            if not isinstance(enemy, NewEnemy):
                raise self.INVALIDOBJECT('Please make sure all enemies in the list are instances of the NewEnemy class.')
            
        self.player.beginFight(playerAttacksFirst, range_)
            
        if playerAttacksFirst:
            self.player.focusOnEnemy(enemies)
        
        else:
            pass
        
        
    def updateLastMove(self, dir_):
        self.lastMove = dir_
        
    def displayInventory(self):
        self.inventoryManager.displayInventory()

def fp(text):
    print('\n' + str(text))
    
room1 = Room('Room One', 'fr', 'Welcome to Room 1')
room2 = Room('Room Two', 'lf', 'Welcome to Room 2', 'l', actionText='Would you like to loot the room?')
room3 = Room('Room Three', 'f', 'Welcome to Room 3!')

map1 = [[room1, room2],
        [0,     room3]]   

room1Loot = LootRoom('Ammo', room2, 'You find and open an ammo crate!', 10, lootOnEnter=True)

enemyType1 = EnemyType('pseudoid', 5, damageWithClose=2, skillLevel=25, pointsPerKill=15)

enemy1 = NewEnemy('pseudoid')

enemy2 = NewEnemy('pseudoid')

print(enemy1.counterClose())

cluster1 = RoomCluster(map1)

obj = TextAdventureGameEngine(room3, cluster1)

obj.fight([enemy1, enemy2], True)
