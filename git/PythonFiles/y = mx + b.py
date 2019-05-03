from fractions import Fraction


### Comments: everything works so far, for example slope can be either pos. or negative. Testing the y-intercept. 
###: Next; Fix it so it can do single digits
print('Welcome to the Slope-Intercept Former! Please write like this:(x,y) or y/x (slope)')
while True:
    opt = input('''Do you have two points, or a slope and a point? Press '1' if you have two points. Press '2' if you have a slope and a point: ''')
    if opt == '1':
        p11 = input('What is your first coordinate?:')

## Next line is the negative
    
        x2 = p11[1:2]
        if x2 == '-':
            x2 = p11[2:3]
            fx2 = '-' + x2
        
        else:
            fx2 = x2
            pass
        x2 = p11[1]
        if x2 == '-':
            y2 = p11[4]
            if y2 == '-':
                fy2 = p11[5]
                fy2 = '-' + fy2
            else:
                fy2 = y2
        
        
        elif x2 != '-':
            y2 = p11[3]   
            if y2 == '-':
                fy2 = p11[4]
                fy2 = '-' + fy2
            else:
                fy2 = y2
        cord1 = '(' + fx2 + ',' + fy2 + ')'
    
    ## Above is GOOD ;)
        
        p12 = input('What is your second coordinate?:')
        x1 = p12[1:2]
        if x1 == '-':
            x1 = p12[2:3]
            fx1 = '-' + x1
        
        else:
            fx1 = x1
            pass
        x1 = p12[1]
        if x1 == '-':
            y1 = p12[4]
            if y1 == '-':
                fy1 = p12[5]
                fy1 = '-' + fy1
            else:
                fy1 = y1
            
            
        elif x1 != '-':
            y1 = p12[3]   
            if y1 == '-':
                fy1 = p12[4]
                fy1 = '-' + fy1
            else:
                fy1 = y1
        cord2 = '(' + fx1 + ',' + fy1 + ')'

    ### Above is GOOD ;)
        
        points = [fy1, fy2, fx1, fx2]
        
    ### Points = 1 = second, vise versa
        
        if fy2 == 0:
            print('Your line is undefined.')
            
        elif fx1 == fx2 and fy1 == fy2:
            print('These points are the same.')
            exit()
            
        elif fx2 == fx1:
            print('Your line is vertical or undefined, which means your equation is: x = ' + fx1)
            exit()
        elif fy2 == fy1:
            print('Your line is horizontal or slope of 0, which means your equation is: y = ' + fy1)
            exit()
       
            
         
        upper = int(fy2) - int(fy1)
        lower = int(fx2) - int(fx1)
        slope = int(upper) / int(lower)
        slope = Fraction(slope).limit_denominator(100)

    ### (Above) Slope

       
        mx = slope * int(fx1)
        
    ### First equation part (above)
        
        b = int(fy1) - mx
        b = Fraction(b)
        b = str(b)
        
        if b[0] == '-':
            slope = str(slope)
            b = str(b)
            ymxb = 'y = ' + slope + 'x ' + b
        elif b[0] != '-':
            ymxb = 'y = ' + str(slope) + 'x + ' + b
        if b[1:2] == '.' or b[2:3] == '.':
            b = Fraction(b).limit_denominator(100)
            slope = str(slope)
            ymxb = 'y = ' + slope + 'x ' + b
            b = str(b)
                    
        print('The y-intercept (b) is: ' + b)
        print('-----------------------------------')
        print('The slope of this line is: ' + str(slope))
        print('-----------------------------------')
        print('The equation of this line in y = mx + b format is:')
        print(ymxb)

    ### 1 WORKS !!! :)
        
    elif opt == '2':
        slope2 = input('''What is your slope?: ''')
        if slope2[0:1] == '-' and slope2[2:3] == '/':
            slope2f = str(int(slope2[1:2]) / int(slope2[3:4]) * -1)
        
        else:
            if slope2[1:2] != '/' or slope2[0:1] != '/':
                if slope2[0:1] == '-':
                    slope2f = slope2[1:2] * -1
                elif slope2[0:1] != '-':
                    slope2f = slope2[0:1]
            else:
                slope2f = int(slope2[0:1]) / int(slope2[2:3])
   

    ### Above Works :)

        b2 = input('''What is your coordinate?: ''')

    ### Both negative
        
        if b2[0:1] and b2[4:5] == '-':
            b2f = str('-' + b2[2:3])
            b3f = str('-' + b2[5:6])

    ### first neg.

        elif b2[1:2] == '-':
            b2f = str('-' + b2[2:3])
            b3f = str(b2[4:5])

    ### second negative

        elif b2[3:4] == '-':
            b2f = str(b2[1:2])
            b3f = str('-' + b2[4:5])

    ### all positive

        elif b2[1:2] and b2[3:4] != '-':
            b2f = str(b2[1:2])
            b3f = str(b2[3:4])

        else:
            print('Error')

    ### Above Works :)
        slope2f = str(slope2f)
        if slope2f[0:1] == '-':
            slope2f = slope2[0:2]
            slope2f1 = slope2[3:4]
            slope2f = str(int(slope2f) / int(slope2f1))

        slope2f = slope2f
        mx2 = int(b2f) * slope2f
        mx2 = str(mx2)
        mx2 = Fraction(mx2)
        eq2 = int(b3f) - mx2
        slope2f = Fraction(slope2f)
        mx2 = str(mx2)
        eq2 = str(eq2)
        
        if b2f == '0':
            slope2f = '0'
        if slope2f == '0':
            check1 = False
        else:
            check1 = True
        if eq2[0:1] == '-':
            check2 = False
        else:
            check2 = True
        slope2f = str(slope2f)
        if slope2f[0:1] == '.' or slope2f[1:2] == '.':
            slope2f = Fraction(slope2f)
        if eq2 == '0':
            check3 = False
        else:
            check3 = True
        print('The y-intercept of this line is: ' + eq2)
        print('------------------------------------')
        
        if check3 == False and check1 == True and check2 == True:                         
            print('The equation of this line in y = mx + b format is: y = '  + str(slope2f) + 'x ')
        elif check1 == True and check2 == True:
            print('The equation of this line in y = mx + b format is: y = '  + str(slope2f) + 'x + ' + str(eq2))
        if check1 == False:                                                                                                                      
            print('The equation of this line in y = mx + b format is: y = ' + str(eq2))                                     
        if check1 == True and check2 == False:
            eq2 =  '- ' + eq2[1:30]
            print('The equation of this line in y = mx + b format is: y = '  + str(slope2f) + 'x ' + str(eq2))
        
        
        exitr1 = input('Would you like to exit or submit a question?: ')                                    
        if exitr1.lower() == 'exit' or exitr1.lower() == 'leave':   
            exit()
        if exitr1.lower() == 'submit' or exitr1.lower() == 'stay' or exitr1.lower() == 'return':
            continue
    elif opt.lower() == 'exit':
        exit()
    else:                                                               
        exitr = input('Would you like to exit or submit a question?: ')

        if exitr.lower() == 'exit' or exitr.lower() == 'leave':
            exit()
        elif exitr.lower() == 'submit' or exitr.lower() == 'stay' or exitr.lower() == 'return':
            continue

