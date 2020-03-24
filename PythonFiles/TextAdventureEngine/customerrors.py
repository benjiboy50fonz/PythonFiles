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

        class EnemyTypeDoesNotExist(Exception):
            pass

        self.INVALIDDIRECTIONSTRING = InvalidDirectionString
        self.INVALIDMAPTYPE = InvalidMapType
        self.INVALIDOBJECT = InvalidObject
        self.INVALIDROOMGIVEN = InvalidRoomGiven
        self.YOUBROKETHEINVENTORY = YouBrokeTheInventory
        self.INVALIDSTRINGGIVEN = InvalidStringGiven
        self.TWONONETYPESGIVEN = TwoNoneTypesGiven
        self.SKILLLEVELNOTPOSSIBLE = SkillLevelNotPossible
        self.ENEMYTYPEDOESNOTEXIST = EnemyTypeDoesNotExist
