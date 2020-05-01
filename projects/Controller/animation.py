import pygame

from pygame.locals import *

class AnimationManager:
    
    def __init__(self):
        self.player = Player()
        
        self.player.rect.x = 375
        self.player.rect.y = 450
        
        self.minLeft = 0 
        self.minTop = 0
        self.maxRight = 750
        self.maxBottom = 500
        
        pygame.init()
        pygame.display.init()
        
        self.screen = pygame.display.set_mode(size=(self.maxRight, self.maxBottom))
        
        pygame.display.update()
        
        self.botsAndPlayer = pygame.sprite.Group()
        
        self.botsAndPlayer.add(self.player)
        
    def loop(self):
        self.update()
        
        self.screen.fill((0, 0, 0))

        self.botsAndPlayer.draw(self.screen)
        
        self.flip()
        
    def update(self):
        self.botsAndPlayer.update()
        
    def shoot(self, s):
        if self.player.shoot(s):
            self.botsAndPlayer.add(self.player.activeBullets[-1])
        
    def bulletPhysics(self):
        self.player.moveBullets()
        
    def flip(self):
        pygame.display.flip()
        
    def movePosition(self, x=0, y=0):        
        if self.player.rect.x + x > self.minLeft and self.player.rect.x + x + 50 < self.maxRight:
            self.player.rect.x += x
            
        if self.player.rect.y + y > self.minTop and self.player.rect.y + y + 20 < self.maxBottom:
            self.player.rect.y += y
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.activeBullets = []
        
        self.shootDelay = 1000 # Milliseconds
        
        self.shootTime = -1 * self.shootDelay
        
        self.image = pygame.Surface((50, 20))
        self.image.fill((255, 255, 255))

        pygame.draw.rect(self.image, (255, 255, 255), [100, 100, 20, 10]) 

        self.rect = self.image.get_rect()
        
    def moveBullets(self):
        deletes = []
        for bullet in self.activeBullets:
            if bullet.y - 5 <= 0:
                deletes.append(bullet)
            else:
                bullet.updatePosition(-5)
            
        for obj in deletes:
            self.activeBullets.remove(obj)
    
    def shoot(self, shootSpeed):
        if shootSpeed < -0.65 and pygame.time.get_ticks() > self.shootTime + self.shootDelay:
            self.activeBullets.append(Bullet(self.rect.x, self.rect.y))
            return True
        return False

class Bullet(pygame.sprite.Sprite):
    def __init__(self, startX, startY):   
        super().__init__()
    
        self.x = startX + 25
        self.y = startY
    
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 0, 255))
        
        pygame.draw.circle(self.image, (0, 0, 255), (self.x, self.y), 2)
        
        self.rect = self.image.get_rect()
        
    def updatePosition(self, yIncrement):
        pygame.draw.circle(self.image, (0, 0, 255), (self.x, self.y + yIncrement), 2)
        pygame.display.update()
        
        

class Enemy: 
    pass
