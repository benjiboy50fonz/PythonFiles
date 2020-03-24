import sys

from .enemy import EnemyType

sys.path.insert(1, '/home/benji/Git/PythonFiles/PythonFiles/TextAdventureEngine') # Allows an import of the custom error and room stuff.

from customerrors import CustomErrors

class NewEnemy(EnemyType):
    
    totalEnemies = set([])
    
    def __init__(self, id_):
        
        super().safeDeclare()
        
        self.id_ = id_
                                
        self.dict_ = super().getListOfEnemies()
        self.instances = super().getinstances()
        
        if id_ not in self.dict_.keys():
            raise self.ENEMYTYPEDOESNOTEXIST('The enemy type has not been instantiated with the the EnemyType.')

        self.createEnemy()
        
    def createEnemy(self):
        listOfData = self.dict_[self.id_]
        
        super().__init__(self.id_, listOfData[0], listOfData[1], listOfData[2], listOfData[3], listOfData[4], accessClass=True)
