import sys, os
sys.path.append('/path/to/Programs')
import Programs


#from Programs.RobotPracFunc import Name

class Command():

    def __init__(self, givenname):
        self.givenName = givenname

    def initialize(self):
        mes = Programs.Name()
        print(mes)

