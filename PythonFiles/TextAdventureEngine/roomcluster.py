from customerrors import CustomErrors

from room import Room

class RoomCluster(CustomErrors):
        
        def __init__(self, map_):                        
            super().__init__()
        
            '''
            Room groupings that are created by a list nested inside another. The nesting list is the x-axis, and the parent list is the y-axis. Insert room objects in these lists, any empty space should be a zero or None.
            '''
             
            if type(map_) != list: # Ensures that this is a true cluster.
                raise self.INVALIDMAPTYPE('Failed to build room cluster. Please ensure that the map type is correct (spoiler alert, it\' not.)')
             
            try:
                if type(map_[0]) != list:
                    raise self.INVALIDMAPTYPE('You must nest a list inside of a list when creating clusters. Like this: \'[[Room1, Room2, Room3]]\'!')
            except(IndexError):
                raise self.INVALIDMAPTYPE('You must nest a list inside of a list when creating clusters. Like this: \'[[Room1, Room2, Room3]]\'!')
            
            # Make sure the structure has equal levels (hard to explain lol)!
            setLength = len(map_[0])
            for row in map_:
                if len(row) != setLength:
                    raise self.INVALIDMAPTYPE('Please make sure each row in the map has the same number of objects. Fill empty spaces with zeroes or Nones.')
            
            # Make sure that all values are objects are 0s, Nones, or objecs.
            for row in map_:
                for room in row:
                    print(isinstance(room, Room))
                    if room != 0 and room != None and not isinstance(room, Room):
                        raise self.INVALIDMAPTYPE('Please make sure all objects in the map are either zeroes, Nones, or Room objects. I have a feeling they\'re not...')
            
            # And after a huge series of tests, my child, YOU are an attribute!!!
            
            self.map_ = map_
            
def fp(text):
    print('\n' + str(text))
