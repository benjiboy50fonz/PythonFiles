class CustomErrors:
    def __init__(self):
        class InvalidDirectionString(Exception):
            pass
        
        class InvalidMapType(Exception):
            pass
        
        class InvalidObject(Exception):
            pass
        
        class InvalidRoomGiven(Exception):
            pass
        
        class YouBrokeTheInventory(Exception):
            pass
        
        class InvalidStringGiven(Exception):
            pass
        
        class TwoNoneTypesGiven(Exception):
            pass
        
        class SkillLevelNotPossible(Exception):
            pass
        
        class InventoryItemsWithTheSameNameDoNotMatch(Exception):
            pass
        
        class InvalidWeaponRangeProvided(Exception):
            pass
        
        self.INVALIDDIRECTIONSTRING = InvalidDirectionString
        self.INVALIDMAPTYPE = InvalidMapType
        self.INVALIDOBJECT = InvalidObject
        self.INVALIDROOMGIVEN = InvalidRoomGiven
        self.YOUBROKETHEINVENTORY = YouBrokeTheInventory
        self.INVALIDSTRINGGIVEN = InvalidStringGiven
        self.TWONONETYPESGIVEN = TwoNoneTypesGiven
        self.SKILLLEVELNOTPOSSIBLE = SkillLevelNotPossible
        self.INVENTORYITEMSWITHTHESAMENAMEDONOTMATCH = InventoryItemsWithTheSameNameDoNotMatch
        self.INVALIDWEAPONRANGEPROVIDED = InvalidWeaponRangeProvided

    def safeDeclare(self):
        class EnemyTypeDoesNotExist(Exception):
            pass
        
        self.ENEMYTYPEDOESNOTEXIST = EnemyTypeDoesNotExist
