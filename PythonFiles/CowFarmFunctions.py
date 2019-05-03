import random
from CowFarmClass import Cows
from CowFarmClass import Cows2

def CowBabyCount():
    bachek = None
    count = random.randint(0,1)
    if count == 0:
        print('Mating did not result in a baby cow.')
        bachek = False
    elif count == 1 and bachek != False:
        mof = random.randint(0,2)
        if mof == 0:
            bg = 'male'
        else:
            bg = 'female'
        print('You got one baby cow! It is a ' + bg + '!')
       

        
