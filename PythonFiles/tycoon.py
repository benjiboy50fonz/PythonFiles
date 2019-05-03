from tycoonchar import Character
from tycoonManual import gameManual

gameRunning = True
turnCount = 0

print('\nWelcome to the Automobile Tycoon!\n\n --------------------------------')
name = str(input("What would you like to name your character? (first AND last name please!): "))

firstName = str(name).split()[0]

try:
    lastName = str(name).split()[1]
except IndexError:
    lastName = firstName

ageIsWrong = True

gender = str(input('\nIs ' + str(firstName[0].upper()) + str(firstName[1:].lower()) + ' ' + str(lastName[0].upper()) + str(lastName[1:].lower()) + ' a male or female? (default is male!): '))

if gender.lower() != 'male' or gender.lower() != 'female':
    gender = 'male'

while ageIsWrong:
    try:
        age = int(input('\nHow old is ' + str(name[0].upper()) + str(name[1:].lower()) + '?: '))
    except ValueError:
        continue
    break

brand = str(input('\nWhat would you like to name your company?: '))
startingProduct = str(input('\nWhat product would you like to begin selling? (please make it a vehicle, ex. \'yachts\'!): '))

player = Character(gender, firstName, lastName, brand, startingProduct, age)
print('\nHere\'s the jist of things...\n')
gameManual()

while gameRunning:
    if turnCount == 0:
        pass
    else:
        
        # insert Turn here!
