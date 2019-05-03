import random
total = 0
comp = False
while not comp:
    ra1 = random.randint(0,1000001)
    ra2 = random.randint(0,1000001)
    total += 1
    print(str('1 = ' + str(ra1)))
    print(str('2 = ' + str(ra2)))
    if ra1 == ra2:
        print('Completed! 1 = ' + str(ra1) + ' and 2 = ' + str(ra2) + '\nThis took ' + str(total) + ' tries!')
        comp = True
        total = 0
    
    else:
        continue
        comp = False
