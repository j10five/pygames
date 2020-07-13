import pygame
from pygame import mixer
import random

pygame.init()

# game
screen = pygame.display.set_mode((800,600))
background = pygame.image.load('riverbank.png')

# player
playerImg = pygame.image.load('fisher.png') #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
playerX = 1
playerY = 180
playerX_change = 0
playerY_change = 0
playerspeed = 1

def player(x, y):
    screen.blit(playerImg, (x, y))

# shell
shellImgList = ['shell1a.png','shell1b.png','shell1c.png','shell2a.png','shell2b.png','shell2c.png','shell3a.png','shell3b.png','shell3c.png']
shellXList = [1, 35, 50, 75, 100, 145, 170, 210, 255, 275, 305, 340, 380, 425, 500, 550, 600, 680, 700, 780]
shellYList = [195, 220, 330, 365, 390, 415, 432, 456, 478, 499, 515, 530, 540, 550, 560, 570, 580, 590, 280, 345]
shellCount = 20

def shell(i, x, y):
    screen.blit(pygame.image.load (i), (x, y)) 
    print(x, y, i)
    
        
running = True
while running:
    screen.fill((204, 229, 255)) # rgb parameters
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change -= playerspeed
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = playerspeed
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change -= playerspeed
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = playerspeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d: 
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_w:
                playerY_change = 0
    playerX += playerX_change
    if playerX <= 1:
        playerX = 1
    if playerX >= 760:
        playerX = 760
    playerY += playerY_change
    if playerY <= 180:
        playerY = 180
    if playerY >= 560:
        playerY = 560
    player(playerX, playerY)
    for i in range(shellCount):
        shellImg = (shellImgList[random.randint(0,8)])
        shellX = shellXList[random.randint(0,19)]
        shellY = shellYList[random.randint(0,19)]
        shell(shellImg, shellX, shellY)
        print(shellCount)
        
             
    pygame.display.update()