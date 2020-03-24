import sys

from enemy import EnemyType

sys.path.insert(1, '/home/benji/Git/PythonFiles/PythonFiles/TextAdventureEngine') # Allows an import of the custom error and room stuff.

from customerrors import CustomErrors

class NewEnemy(EnemyType, CustomErrors):
    def __init__(self, id_):
                        
        super().__init__(id_, accessClass=True)
                        
        self.dict_ = super().getListOfEnemies()
        
        if id_ not in self.dict_.keys():
            raise self.ENEMYTYPEDOESNOTEXIST('The enemy type has not been instantiated with the the EnemyType.')

    def get(self):
        print(str(self.dict_))
        
en = NewEnemy('ene')
en.get()
