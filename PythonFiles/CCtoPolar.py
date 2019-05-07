import math

def convert(x, y):
    r = math.sqrt((x**2) + (y**2))
    theta = math.degrees(math.atan(y / x))
    string = 'R = ' + str(r) + ' Theta = ' + str(theta)

    return string
    
x = input('X: ')
y = input('Y: ')

print(convert(int(x), int(y)))    
