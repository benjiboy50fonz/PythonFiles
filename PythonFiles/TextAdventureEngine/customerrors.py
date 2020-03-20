class CustomErrors:
    def __init__(self):
        class InvalidDirectionString(Exception):
            pass
        
        class InvalidMapType(Exception):
            pass
        
        class InvalidObject(Exception):
            pass

        self.INVALIDDIRECTIONSTRING = InvalidDirectionString
        self.INVALIDMAPTYPE = InvalidMapType
        self.INVALIDOBJECT = InvalidObject
