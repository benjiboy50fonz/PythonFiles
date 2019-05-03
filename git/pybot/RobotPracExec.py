import sys, os
sys.path.append('/path/to/Programs')
from Programs.robotpraccommand import Command

#from Programs.RobotPracCommand import Command

begin = input(''' Press 's' to run the 'Welcome Command!''')
if begin.lower() == 's':
    getname = input('Hi, what is your name?')
    getname = str(getname)
    Command(getname)
    print('Completed')
    
