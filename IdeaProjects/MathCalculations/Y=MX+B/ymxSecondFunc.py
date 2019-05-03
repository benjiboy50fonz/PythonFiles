from fractions import Fraction

def second_op():
    finish2 = True
    def get_slope(x1, x2, y1, y2):
        upper = y2 - y1
        upper = int(upper)
        lower = x2 - x1
        lower = int(lower)
        slope = float(upper) / float(lower)
        if '.' in str(slope):
            fslope = Fraction(slope).limit_denominator(100000)
            # fslope = slope
        else:
            fslope = slope
        return fslope

    try:
        x1i = input('''What is your 1st point's x-coordinate?: ''')
        x1i = int(x1i)
        y1i = input('''What is your 1st point's y-coordinate?: ''')
        y1i = int(y1i)
        x2i = input('''What is your 2nd point's x-coordinate?: ''')
        x2i = int(x2i)
        y2i = input('''What is your 2nd point's y-coordinate?: ''')
        y2i = int(y2i)
    except SyntaxError:
        print('Please enter numbers!')
        finish2 = False
        return finish2
    sloper = get_slope(x1i, x2i, y1i, y2i)
    # --- Solving Equation ---
    mx2 = sloper * x1i
    b22 = y1i - mx2
    if '.' in str(b22):
        b22 = Fraction(b22).limit_denominator(10000)

    b22 = str(b22)
    if '-' in b22:
        equation2 = 'y = ' + str(sloper) + 'x - ' + b22[1::]
    else:
        equation2 = 'y = ' + str(sloper) + 'x + ' + b22
    # --- Printing ---

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


