from random import randint
from random import choice
import random
# Imports all for assurance :)


def answers(correct, in1, in2, in3):
    gopt = random.randint(0, 3)
    print(gopt)
    if gopt == 0:
        anstr = '   A. ' + str(correct) + '     B. ' + str(in1) + '\n\n   C. ' + str(in2) + '     D. ' + str(in3)
        anstr = str(anstr)
    elif gopt == 1:
        anstr = '   A. ' + str(in1) + '     B. ' + str(correct) + '\n\n   C. ' + str(in2) + '     D. ' + str(in3)
        anstr = str(anstr)
    elif gopt == 2:
        anstr = '   A. ' + str(in1) + '     B. ' + str(in2) + '\n\n   C. ' + str(correct) + '     D. ' + str(in3)
        anstr = str(anstr)
    elif gopt == 3:
        anstr = '   A. ' + str(in1) + '     B. ' + str(in2) + '\n\n   C. ' + str(in3) + '     D. ' + str(correct)
        anstr = str(anstr)
    else:
        print('error')
    return anstr


def start():
    print('Welcome to the test generator! ')
    print(' ')
    repe = True
    while repe == True:
        print(' ')
        starto = input('''There are multiple options for the format of the test. Enter '1' for a name, date, and period, enter '2' for a name and date, or enter '3' for only a name!: ''')
        if starto == '1':
            print(' ')
            retc = input('''You will have a name, date, and period on your test!\nType 'ok', if this is correct! Not correct? Type 'return'!: ''')
            if retc.lower() == 'ok':
                repe = False
                pass
            elif retc.lower() == 'return':
                continue
        elif starto == '2':
            print(' ')
            retc = input('''You will have a name and a date on your test!\nType 'ok', if this is correct! Not correct? Type 'return'!: ''')
            if retc.lower() == 'ok':
                repe = False
                pass
            elif retc.lower() == 'return':
                continue
        elif starto == '3':
            print(' ')
            retc = input('''You will have only a name on your test!\nType 'ok', if this is correct! Not correct? Type 'return'!: ''')
            if retc.lower() == 'ok':
                repe = False
                pass
            elif retc.lower() == 'return':
                continue
    print('''\nGreat! Let's continue!''')
    if starto == '1':
        ret = 1
    elif starto == '2':
        ret = 2
    elif starto == '3':
        ret = 3
    else:
        print('error')

    return ret

beg = start()
name = input('\nWhat would you like to name this file?: ')
name1 = name + '.pdf'
file = open(name1, 'w+')
rando = input('''\nWould you like to randomize the order of the questions? Type 'yes' if so! If not, type anything!: ''')
if rando.lower() == 'yes':
    print('\nOrder randomized!')
    randm = True
else:
    randm = False
questions = {}
ansls = []
qs = True
while qs == True:
    question = input('''Add a question! If you are finished, type 'done'!: ''')
    if question.lower() == 'done':
        qs = False
        break
    ans = input('''What is the correct answer for this question?: ''')
    ansls.append(ans)
    questions[question] = ans
    num = 0
reversed(sorted(questions.keys()))
if beg == 1:
    file.write(' ' + str(name) + '\n\n Name:_______________________   Date:________   Period:________ \n\n')
    for i in questions:
        answer = questions.get(str(i))
        randoption = random.choice(ansls)
        if len(questions) < 4:
            if len(questions) == 1:
                mc = answers(answer, 'N/A', 'N/A', 'N/A')
            elif len(questions) == 2:
                mc = answers(answer, random.choice(ansls), 'N/A', 'N/A')
            elif len(questions) == 3:
                mc = answers(answer, random.choice(ansls), random.choice(ansls), 'N/A')
            elif len(questions) >= 4:
                mc = answers(answer, randoption, randoption, randoption)
        print('here')
        
        num += 1
        file.write(' ' + str(num) + ') ' + str(i) + '\n\n' + str(mc) + '\n\n')
elif beg == 2:
    file.write(' ' + str(name) + '\n\n Name:_______________________   Date:________                   \n\n')
    for i in questions:
        answer = questions.get(str(i))
        randoption = random.choice(ansls)
        if len(questions) < 4:
            if len(questions) == 1:
                mc = answers(answer, 'N/A', 'N/A', 'N/A')
            elif len(questions) == 2:
                mc = answers(answer, random.choice(ansls), 'N/A', 'N/A')
            elif len(questions) == 3:
                mc = answers(answer, random.choice(ansls), random.choice(ansls), 'N/A')
            elif len(questions) >= 4:
                mc = answers(answer, randoption, randoption, randoption)
        print('here')
        
        num += 1
        file.write(' ' + str(num) + ') ' + str(i) + '\n\n' + str(mc) + '\n\n')

elif beg == 3:
    file.write(' ' + str(name) + '\n\n Name:_______________________                                   \n\n')
    for i in questions:
        answer = questions.get(str(i))
        randoption = random.choice(ansls)
        if len(questions) < 4:
            if len(questions) == 1:
                mc = answers(answer, 'N/A', 'N/A', 'N/A')
            elif len(questions) == 2:
                mc = answers(answer, random.choice(ansls), 'N/A', 'N/A')
            elif len(questions) == 3:
                mc = answers(answer, random.choice(ansls), random.choice(ansls), 'N/A')
            elif len(questions) >= 4:
                mc = answers(answer, randoption, randoption, randoption)
        print('here')
        
### TODO: Set option for format as 2 x 2, or 4 x 1!!!
        
        num += 1
        file.write(' ' + str(num) + ') ' + str(i) + '\n\n' + str(mc) + '\n\n')
file.close()
file = open(name1, 'r')
contents = file.read()
print(contents)
