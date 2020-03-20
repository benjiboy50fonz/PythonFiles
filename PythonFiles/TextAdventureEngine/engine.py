from customerrors import CustomErrors

from room import Room
from roomcluster import RoomCluster

class TextAdventureGameEngine(CustomErrors):
    
    '''
    Key, universal terms for directions:
    Left: 'l'
    Right: 'r'
    Forward: 'f'
    Back: 'b'
    Unknown: '!'
    '''

                
    def __init__(self, startRoom, startMap, searchables=[], allowBack=True, defaultDirections=None):
        super().__init__()
        
        self.errorEngine = CustomErrors()
        
        self.startRoom = startRoom
        self.startMap = startMap
        
        if not isinstance(self.startRoom, Room):
            raise self.INVALIDOBJECT('Please pass an object of the Room class!')
        
        self.currentRoom = self.startRoom.name
        
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
        for char in str(dirString.lower()).strip():
            if char not in self.globalKnowns:
                raise self.INVALIDDIRECTIONSTRING('Invalid character in string. Please refer to the global characters.') # Raise a custom, invalid direction string error
            
        normalizedEntry = self.interpretDirection(rawEntry)
        

def fp(text):
    print('\n' + str(text))

room1 = Room('Room One', 'flr', 'Welcome to Room 1')
room2 = Room('Room Two', 'lfr', 'Welcome to Room 2')

map1 = [[room1, room2]]       

cluster1 = RoomCluster(map1)
    
obj = TextAdventureGameEngine(room1, cluster1)
