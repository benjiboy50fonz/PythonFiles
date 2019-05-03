from fractions import Fraction

def first_op():
    finished_c = True
    try:
        slope1 = raw_input('''What is your slope?(Please write like this: '(-)x/(-)y' : ''')
    except SyntaxError:
        finished_c = False
        return finished_c
    ss = 0
    sss = 0
    sss2 = -1
    count = True
    slope1 = str(slope1)
    if '/' not in slope1:
        slope1 = slope1 + '/1'
    base = 0
    while count:
        if '/' == slope1[ss]:
            print('Error: Please enter slope in the given form!')
            count = False
            raise ValueError
        else:
            solve = True
            while solve:
                try:
                    find = slope1[0:sss]
                except IndexError:
                    slope1 = str(slope1) + '/1'
                    find = slope1[sss]

                if '/' not in find:
                    # base = "{0}{1}".format(str(base), str(find))
                    sss += 1
                    continue
                elif '/' in find:
                    find = find[:-1]
                    xs = find

                try:
                    find2 = slope1[sss2:]
                except IndexError:
                    finished_c = False
                    return finished_c
                if '/' not in find2:
                    sss2 -= 1
                    continue
                elif '/' in find2:
                    find2 = find2[1:]
                    ys = find2
                    solve = False
                solve = False
                count = False
            # xs = base[1::]
        count = False
    try:
        ys = float(ys)
        xs = float(xs)
        fs = xs / ys
    except (TypeError, ValueError):
        print('Unknown Error! Please review form and try again!')
        finished_c = False
        return finished_c
    # except NameError:
    #   fs = 0

    # --- Goes to Coordinates ---
    try:
        c1x = input('What is your x-coordinate?: ')
        c1x = int(c1x)
        c1y = input('What is your y-coordinate?: ')
        c1y = int(c1y)
    except (NameError, SyntaxError):
        print('Please enter numbers!')
        finished_c = False
        return finished_c

    # --- Goes To Equation ---

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

    # --- Math Done ---

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

