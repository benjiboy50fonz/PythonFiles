import sys, os
sys.path.append('/path/to/Programs')
import RobotPracFunc


from RobotPracFunc import Name

class Command():

    def __init__(self, givenname):
        self.givenName = givenname

    def initialize(self, givenname):
        self.mes = Name(givenname)
        print(self.mes)


