#!/usr/bin/env python3

import pygame

from pygame.locals import *

from animation import AnimationManager
from controls import ControlManager

am = AnimationManager()
cm = ControlManager()

movementKeys = [K_RIGHT, K_LEFT]

def eventHandler():
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()
            
    x, y = cm.move()
    am.movePosition(x, y)
    
    am.shoot(cm.getTrigger())
    am.bulletPhysics()
    
    #keys = pygame.key.get_pressed()

    #for key in movementKeys:
        #if keys[key]:
            #cm.registerMotion(pygame.key.name(key))
            #cm.received.append(pygame.key.name(key))
            
    #cm.checkExpecting()
    #cm.received = []
    
    # Animations based off holding below.

    
while True:
    eventHandler()
    am.loop()
    
    pygame.display.flip()
