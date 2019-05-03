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
print(cord2)
    
