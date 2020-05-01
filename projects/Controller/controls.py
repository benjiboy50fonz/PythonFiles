import pygame

class ControlManager:
    
    def __init__(self): 
        
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            print('Plug In A Controller Before you Begin!')
            pygame.quit()
            exit()

        self.myStick = pygame.joystick.Joystick(0)
        self.myStick.init()

        self.holding = {
                        'right':False,
                        'left':False
                        }
        
        self.expecting = []
        self.received = []
        
        self.maxSpeed = 10
        
    def registerMotion(self, string):
        if not self.holding[string]:
            self.toggleMotion(string)
            self.expecting.append(string)
    
    def move(self):
        
        x = self.getX() * self.maxSpeed
        y = self.getY() * self.maxSpeed
        
        if abs(x) <= 1.77:
            x = 0
        if abs(y) <= 1.77:
            y = 0
        
        return x, y
    
    def checkExpecting(self):
        for obj in self.expecting:
            if obj not in self.received:
                self.toggleMotion(obj)
                self.expecting.remove(obj)
                
    def getX(self):
        return self.myStick.get_axis(0)
    
    def getY(self):
        return self.myStick.get_axis(1)
    
    def getTrigger(self):
        return self.myStick.get_axis(5)
        
    def toggleMotion(self, string):
        self.holding[string] = not self.holding[string]

    
