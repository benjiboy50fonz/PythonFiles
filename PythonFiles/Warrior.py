class Warrior(object):
    name = ''
    age = 0
    gender = ''
    role = ''

    def __init__(self, name, age, gender, role):
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role
        
    def ListMySoldiers(self):
        print('Your warriors are:\n' + self.name + ': ' + self.age + ' years old, ' + self.gender + ', ' + self.role)        

def make_warrior(name, age, gender, role):
    warrior = Warrior(name, age, gender, role)
    return warrior
while True:
    begin = input('Would you like to recruit a warrior, or see your warriors?: ')
    if begin.lower() == 'recruit':
        name_i = input('What would you like to name this warrior?: ')
        age_i = input('How old is this warrior?: ')
        gender_i = input('Is this a male or a female?: ')
        role_i = input('What type of warrior is this?: ')
        warrior = make_warrior(name_i, age_i, gender_i, role_i)

    elif begin.lower() == 'view':
        try:
            warrior.ListMySoldiers()
            print('Hells Ya!')
        except NameError:
            print('Oof')
            continue
                                                                                                        
