#!/usr/bin/env python3

import pygame
import random
import math

from pygame.locals import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, minWidth, maxWidth, height, gap, force=False):
        super().__init__()
        
        if force:
            self.width = maxWidth
            
        else:
            self.width = random.randint(minWidth, maxWidth)
        
        self.height = height
        
        self.middle = self.width + int(gap / 2)
        
        self.image = pygame.Surface([self.width, self.height])
        
        self.image.fill((255, 0, 0))
        
        pygame.draw.rect(self.image, (255, 0, 0), [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()
        
    def engageSupplementary(self, x, y):
        self.rect.x = x
        self.rect.y = y
        
    def getWidth(self):
        return self.width

    def getHoleMiddle(self): # Only call on mainObj
        return self.middle

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.length = x * 2
        self.height = y + 50
        
        self.maxSpeed = 11
        
        side = 30
        self.radius = side / 2
        
        self.image = pygame.Surface([30, side])
        self.image.fill((255, 255, 255))
                
        pygame.draw.circle(self.image, (0, 0, 255), (15, 15), 15, 0)
        
        self.rect = self.image.get_rect()
        
        self.rect.center = (x, y)
        
        self.standardColor = True
        
    def moveStick(self, val):
        if abs(val) > 0.3 and 0 < self.rect.center[0] < self.length:
            self.rect.center = (self.rect.center[0] + self.maxSpeed * val, self.rect.center[1])
            
        elif abs(val) > 0.3:
            self.rect.center = (self.rect.center[0] + self.maxSpeed * val * -1, self.rect.center[1])
            
    def moveRight(self):
        if self.rect.center[0] + 7 + self.radius <= self.length:
            self.rect.center = (self.rect.center[0] + 7, self.rect.center[1])
        
    def moveLeft(self):
        if self.rect.center[0] - 7 - self.radius >= 0:
            self.rect.center = (self.rect.center[0] - 7, self.rect.center[1])
        
    def setNight(self):
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image, (0, 200, 0), (15, 15), 15, 0)
        
    def setDay(self):
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (0, 0, 255), (15, 15), 15, 0)
            
    def toggleColor(self):
        if self.standardColor:
            self.setNight()
        else:
            self.setDay()
            
        self.standardColor = not self.standardColor
        
class AnimationManager:

    def __init__(self):
        
        pygame.display.init()
        
        self.levelUpped = False
        
        self.level = 1
        
        self.previousMiddleLocation = 0
        self.spacingLimit = 400
        
        self.levels = {2 : [9, 380, 190, 500],
                       3 : [9, 370, 170, 500],
                       4 : [10, 370, 160, 500],
                       5 : [10, 350, 160, 500], 
                       6 : [11, 340, 150, 400],
                       7 : [11, 340, 150, 400],
                       8 : [12, 330, 150, 300],
                       9 : [12, 310, 150, 300],
                       10 : [13, 300, 150, 300]
                       }
        
        self.passed = 0
        
        self.clock = pygame.time.Clock()
        
        self.displayedObstacles = []
        
        self.obstacleHeight = 15
        
        self.startHoleWidth = 200
        
        self.pixelSpacing = 400
        
        self.obstacleSpeed = 8
        
        self.standardBG = True
                
        self.minLeft = 0
        self.minTop = 0
        self.maxRight = 750
        self.maxBottom = 500
        
        self.speed = 5
        
        self.screen = pygame.display.set_mode(size=(self.maxRight, self.maxBottom))
        self.screen.fill((0, 0, 0))
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255, 255, 255))
        
        self.screen.blit(self.background, (0, 0))
            
        pygame.display.update()
        
        self.player = Player(int(self.maxRight / 2), self.maxBottom - 50)
        self.spriteGroup = pygame.sprite.Group(self.player)
        
        self.spriteGroup.draw(self.screen)
    
        pygame.display.flip()
        
        self.clock.tick(50)
        
        self.createNewObstacle()
        
    def toggleBackground(self):
        if self.standardBG:
            self.setDarkBG()
        else:
            self.setStandardBG()
            
        self.standardBG = not self.standardBG
        
    def setDarkBG(self):
        self.background.fill((0, 0, 0))
        
    def setStandardBG(self):
        self.background.fill((255, 255, 255))
        
    def increaseLevel(self):
        self.level += 1
        
        applyThese = self.levels[self.level]
        
        self.obstacleSpeed = applyThese[0]
        self.pixelSpacing = applyThese[1]
        self.startHoleWidth = applyThese[2]
        self.spacingLimit = applyThese[3]
        
        if random.randint(0, 2) == 1:
            self.player.toggleColor()
            self.toggleBackground()
            pygame.display.update()
            
        
    def checkCollision(self):
        interesecting = pygame.sprite.spritecollide(self.player, self.spriteGroup, False)
        if len(interesecting) > 1:
            print('Game Over!')
            print('Level: ' + str(self.passed))
            return True
        
        return False
        
    def progressGame(self):
        if self.passed % 10 == 0 and self.passed != 0 and self.level < 10 and not self.levelUpped:
            print('Level Up! + ' + str(self.passed))
            self.increaseLevel()
            self.levelUpped = True
        
    def moveObstacles(self):
        delete = []
        new = 0
        
        for obstacle in self.displayedObstacles:
            obstacle[0].rect.y += self.obstacleSpeed
            obstacle[1].rect.y += self.obstacleSpeed
            
            if obstacle[0].rect.y >= self.pixelSpacing and obstacle[2]:
                new += 1
                obstacle[2] = False
            
            if not self.minTop < obstacle[0].rect.y < self.maxBottom:
                delete.append(obstacle)
                self.spriteGroup.remove(obstacle[0])
                self.spriteGroup.remove(obstacle[1])
                self.passed += 1
                self.levelUpped = False
                
        for o in delete:
            self.displayedObstacles.remove(o)
            
        for i in range(new):
            self.createNewObstacle()
    
    def createNewObstacle(self): 
        
#        mainObj = Obstacle(0, self.maxRight - self.startHoleWidth, self.obstacleHeight, self.startHoleWidth)
        
        print(str(self.previousMiddleLocation) + ' p ')
        mainObj = Obstacle(max(0, self.previousMiddleLocation - self.spacingLimit), max(self.maxRight - self.startHoleWidth, self.previousMiddleLocation - self.startHoleWidth), self.obstacleHeight, self.startHoleWidth) # I'm a fucking genius

        self.previousMiddleLocation = mainObj.getHoleMiddle()
        print(self.previousMiddleLocation)
        
        supplementaryObj = Obstacle(mainObj.getWidth() + self.startHoleWidth, self.maxRight, self.obstacleHeight, self.startHoleWidth, force=True)
        supplementaryObj.engageSupplementary(mainObj.getWidth() + self.startHoleWidth, 0)
        
        self.spriteGroup.add(mainObj)
        self.spriteGroup.add(supplementaryObj)
        
        self.displayedObstacles.append([mainObj, supplementaryObj, True])
        self.updateDraw()
        
    def clockTick(self):
        self.clock.tick(50)
        
    def movePlayerL(self):
        self.player.moveLeft()
        
    def movePlayerR(self):
        self.player.moveRight()
        
    def movePlayerS(self, val):
        self.player.moveStick(val)
        
    def updateDraw(self):
        self.spriteGroup.clear(self.screen, self.background)
        self.spriteGroup.update()
        self.spriteGroup.draw(self.screen)

    
def gameOver():
    while True:
        pass

am = AnimationManager()

pygame.init()

def eventHandler():
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()
    
    am.clockTick()
    
    if pygame.joystick.get_count() == 0:
            print('Plug In A Controller Before you Begin!')
            pygame.quit()
            exit()
    
    myStick = pygame.joystick.Joystick(0)
    
    myStick.init()
    
    a = myStick.get_axis(3)
            
    am.movePlayerS(a)

    am.moveObstacles()
    
    if am.checkCollision():
        gameOver()
        
    am.progressGame()
    
    am.updateDraw()
    
    pygame.display.flip()
    
pygame.time.wait(3000)
    
while True:
    eventHandler()

