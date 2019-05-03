from CowFarmClass import Cows
from CowFarmClass import Cows2
import random
import CowFarmFunctions

print('Welcome to the Cow Farm!')
cowsls = []
cowg = []
while True:
    opt = input('''What would you like to do? You can add a cow, mate cows to breed, or kill one. PLEASE DO NOT NAME COWS THE SAME. Press '1' to add a cow, '2' to kill a cow, or '3' to mate two cows:''')
    if opt == '1':
        name1 = input('''What is the cow's name?: ''')
        gender1 = input('''Is it a male or a female? (Please type 'male' or 'female'): ''')
        #CHECK
        if gender1 != 'male' and gender1 != 'female':
            print('Please enter male or female.')
            continue
        #CHECK
        age1 = input('''How old is your cow?: ''')
        cowa = Cows()
        cowa.AddCow(name1, gender1, age1)
        
        cowgadd = str(cowa.name) + ' is a ' + str(cowa.gender)

        cowg.append(cowgadd)
        cowsls.append(cowa.name)
        print(cowsls)
        opt2 = input('Would you like to exit or return?: ')
        if opt2.lower() == 'exit':
            print('Bye!')
            exit()
        elif opt2.lower() == 'return' or opt2b.lower() == ' return':
            print(' ')
            print('------------------')
            print('Returning . . . ')
            print('------------------')
            print(' ')
            continue
    elif opt == '2':
        print('Print the number of the cow you would like to kill:')
        print(' ')
        print('-------------------------')
        for i in cowsls:
            print(i)
        print('-------------------------')
        print(' ')
        killwho = input('What is the number of the cow you would like to kill, starting at 1?: ')
        killwho = int(killwho) - 1
        cowsls.pop(int(killwho))
        print(' ')
        meat = random.randint(0,3) 
        if meat == '0':
            prmeat == '1'
            admeat = '1'
        elif meat == '1':
            prmeat = '3'
            admeat = '3'
        else:
            prmeat = '5'
            admeat = '5'
        print('The cow was successfully killed. You got ' + prmeat + ' piece(s) of meat!')
        opt2b = input('Would you like to exit or return?: ')
        if opt2b.lower() == 'exit':
            print('Bye')
            exit()
        elif opt2b.lower() == 'return' or opt2b.lower() == ' return':
            print(' ')
            print('------------------')
            print('Returning . . . ')
            print('------------------')
            print(' ')
            continue
    elif opt == '3':
        print(' ')
        print('---------------')
        print(' ')
        for cow in cowg:
            print(cow)
        print(' ')
        print('---------------')
        print(' ')
        matewho = input('''Please pick one male to mate. Please type the number in which the cow is listed from the top, starting at '1': ''')
        matewho = int(matewho)
        matewho = matewho - 1
        print(' ')
        print('You selected ' + cowsls[matewho])
        print(' ')
        matewho = int(matewho)

#------------------------ SECOND COW(FEMALE) -------------------------
        
        matewho2 = input('''Please pick one male to mate. Please type the number in which the cow is listed from the top, starting at '1': ''')
        matewho2 = int(matewho2)
        matewho2 = matewho2 - 1
        print(' ')
        print('You selected ' + cowsls[matewho2])
        print(' ')
        matewho2 = int(matewho2)

        check1 = input('The two cows you have selected to mate are ' + cowsls[matewho] + ' and ' + cowsls[matewho2] + '. Is this correct?: ')
        if check1.lower() == 'yes':
            pass
        else:
            print(' ')
            print('-------------------------')
            print('Cancelled. Returning. . .')
            print('-------------------------')
            print(' ')
        bachek = None


    #### Function Below --> CowFarmFunctions.CowBabyCount()

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
            name1 = input('What would you like to name your cow?: ')
            cow1 = Cows2()
            cow1.AddCow(name1, bg, '1')
            name2 = name1
        
    ### --- Done
        
        if bachek == False:
            pass
        else:
            cowsls.append(name2)
            print(cowsls)
            print('Done')

    else:
        continue
                         
    if cowg == []:
        print('!!!!!ERROR!!!!!')
        print(' ')
        print('Please add a cow before mating.')
        print(' ')
            
                                                                                                                                                    


    #ERRORS:
    
        

         
        
            
     
                                                                 
