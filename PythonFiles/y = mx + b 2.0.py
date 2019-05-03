from fractions import Fraction

def toInt(num):
    num = int(num)
    return num

while True:
    startop = input('''Welcome to the y = mx + b calculator 2.0! NOTE: IF THERE IS A DIVIDE BY ZERO ERROR, THE PROGAM WILL CRASH!!! Please enter '1' for a slope and a point, or '2' for two points!: ''')
    if startop == '1':
        slope1 = input('''What is your slope?(Please write like this: '(-)x/(-)y: ''')
        ss = 0
        count = True
        while count == True:
            if slope1[ss] == '/':
                print('error')
                count = False
            
            else:
                solve = True
                sss = 0
                base = 0
                while solve == True:
                    find = slope1[sss]
                    if find != '/':
                        base = str(base) + str(find)
                        sss += 1
                        continue
                    else:
                        solve = False
                count = False
                xs = base[1::]
            ys = slope1[sss + 1::]
            count = False
        ys = int(ys)
        xs = int(xs)
        try:
            fs = xs/ys
        except ZeroDivisionError:    
            fs = 000
        
    ### --- Goes to Coordinates ---
        
        c1x = input('What is your x-coordinate?: ')
        c1x = int(c1x)
        c1y = input('What is your y-coordinate?: ')
        c1y = int(c1y)

    ### --- Goes To Equation ---
        
        eq1 = fs * c1x
        eq2 = c1y - eq1
        b = eq2
        b = str(b)
        if '.' in b:
            b2 = Fraction(b).limit_denominator(100000)
            b2 = str(b2)
        else:
            b2 = b
        fs = str(fs)
        if '.' in fs:
            fs2 = Fraction(fs).limit_denominator(100000)
            
        else:
            fs2 = fs
        
        if '-' in b:
            equation = 'y = ' + str(fs2) + 'x - ' + b2[1::]
        else:
            equation = 'y = ' + str(fs2) + 'x + ' + str(b2)

            
        
    ### --- Math Done ---

        if b == 0:
            print(' ')
            print('Slope: ')
            print('m = ' + str(fs))
            print(' --- ')
            print('Y-Intercept: ')
            print('b = 0')
            print(' --- ')
            print('Equation: ')
            print('y = ' + str(fs) + 'x')
        else:
            print(' ')
            print('Slope: ')
            print('m = ' + str(fs2))
            print(' --- ')
            print('Y-Intercept: ')
            print('b = ' + str(b2))
            print(' --- ')
            print('Equation: ')
            print(equation)

    ### --- End First Opt ---

    elif startop == '2':
        def getSlope(x1, x2, y1, y2):
            
            upper = y2 - y1
            upper = int(upper)
            lower = x2 - x1
            lower = int(lower)
            slope = upper / lower
            if '.' in str(slope):
                fslope = Fraction(slope).limit_denominator(100)
                #fslope = slope
            else:
                fslope = slope
            return fslope
        x1i = input('''What is your 1st point's x-coordinate?: ''')
        x1i = int(x1i)
        y1i = input('''What is your 1st point's y-coordinate?: ''')
        y1i = int(y1i)
        x2i = input('''What is your 2nd point's x-coordinate?: ''')
        x2i = int(x2i)
        y2i = input('''What is your 2nd point's y-coordinate?: ''')
        y2i = int(y2i)
        sloper = getSlope(x1i, x2i, y1i, y2i)
    ### --- Solving Equation ---
        mx2 = sloper * x1i
        b22 = y1i - mx2
        if '.' in str(b22):
            b22 = Fraction(b22).limit_denominator(10000)
           
        b22 = str(b22)
        if '-' in b22:
            equation2 = 'y = ' + str(sloper) + 'x - ' + b22[1::]
        else:
            equation2 = 'y = ' + str(sloper) + 'x + ' + b22
        print(b22)    
    ### --- Printing ---
        
        if b22 == 0 or b22 == '0':
            print(' ')
            print('Slope: ')
            print('m = ' + str(sloper))
            print(' --- ')
            print('Y-Intercept: ')
            print('b = 0')
            print(' --- ')
            print('Equation: ')
            print('y = ' + str(sloper) + 'x')
        else:
            print(' ')
            print('Slope: ')
            print('m = ' + str(sloper))
            print(' --- ')
            print('Y-Intercept: ')
            print('b = ' + str(b22))
            print(' --- ')
            print('Equation: ')
            print(equation2)    
            
        
    else:
        print('''Please enter '1' or '2'! \n\n -------------------------------- \n\n ''')
        continue
        
        
