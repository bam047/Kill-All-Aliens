import pygame
from pygame import *
import sys
from pygame.locals import *

mainSurface = pygame.display.set_mode((1000, 1000))
gems = pygame.sprite.Group()
Level1 = True
Level2 = False
Level3 = False
Level4 = False
Level5 = False

class BlueBlaster(pygame.sprite.Sprite):

    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('BlueBlaster.png')
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        for num in range(5):
            mainSurface.blit(self.image, self.rect)
            print "It works"
            self.rect.x += self.speed
            pygame.display.update()
        for num in range(10):
            mainSurface.blit(self.image, self.rect)
            self.rect.x -= self.speed
            pygame.display.update()
        for num in range(5):
            mainSurface.blit(self.image, self.rect)
            self.rect.x += self.speed
            pygame.display.update()
            
        
                

class Level_01():
    def __init__(self):
        self.image = pygame.image.load('space.png')
        for x in range(18):
            Blue = BlueBlaster(50*x+50,50,5)
            gems.add(Blue)
        for x in range(18):
            Blue = BlueBlaster(50*x+50,100,5)
            gems.add(Blue)
        for x in range(18):
            Blue = BlueBlaster(50*x+50,150,5)
            gems.add(Blue)

    def update(self):
        mainSurface.blit(self.image, (0,0))
        print "it works"
            
def main():
    pygame.init()
    pygame.display.set_caption("Kill All Aliens")
    image = pygame.image.load('space.png')
    mainSurface.blit(image, (0,0))
    playerImage = pygame.image.load("player.png")
    playerRect = playerImage.get_rect()
    playerRect.top = 900
    playerRect.left = 500
    speedx = 5


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            playerRect.right += speedx
        if pressed[pygame.K_LEFT]:
            playerRect.left -= speedx
        mainSurface.blit(playerImage,playerRect)
        pygame.display.update()
        Level_01()    

main()
    
