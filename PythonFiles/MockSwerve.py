import math

def convert(x, y):
    r = math.sqrt((x**2) + (y**2))
    theta = math.degrees(math.atan(y / x))
    string = 'R = ' + str(r) + ' Theta = ' + str(theta)

    return string
    
x = input('Joystick X: ')
y = input('Joystick Y: ')
rotate = float(input('Joystick Rotate: '))

# Trackwidth in inches
width = 24

# Wheelbase in inches
length = 25.75

r = math.sqrt((width**2) + (length**2))
try:
    a = math.atan(float(y) / float(x))
except(ZeroDivisionError):
    a = 0
    
theta = math.degrees(a)

fwd = float(y)
strf = float(x)

# NOT field-centric

A = strf - rotate * (length / r)
B = strf + rotate * (length / r)
C = fwd - rotate * (width / r)
D = fwd + rotate * (width / r)

w1s = math.sqrt(B**2 + C**2)
w2s = math.sqrt(B**2 + D**2)
w3s = math.sqrt(A**2 + D**2)
w4s = math.sqrt(A**2 + C**2)

w1a = math.atan2(B, C) * 180 / math.pi
w2a = math.atan2(B, D) * 180 / math.pi
w3a = math.atan2(A, D) * 180 / math.pi
w4a = math.atan2(A, C) * 180 / math.pi

print('''
Speeds:
Front Right: ''' + str(w1s) +
'''\nFront Left: ''' + str(w2s) +
'''\nBack Left: ''' + str(w3s) +
'''\nBack Right: ''' + str(w4s))

print('''
Angles:
Front Right: ''' + str(w1a) +
'''\nFront Left: ''' + str(w2a) +
'''\nBack Left: ''' + str(w3a) +
'''\nBack Right: ''' + str(w4a))
