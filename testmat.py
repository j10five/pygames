import pygame
import random
import math
import time
from pygame import mixer
#initialize pygame module
pygame.init() 

# create the screen w/ width (x-axis), height(y-a xis)
screen = pygame.display.set_mode((800, 600)) 

#Alter Title and Icon - Icons made by <a href="https://www.flaticon.com/free-icon/rafting_2503514" title="monkik">monkik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
pygame.display.set_caption("The River")
icon = pygame.image.load('rafting.png')
pygame.display.set_icon(icon)

#background
background = pygame.image.load('riverbank.png')

# player
playerImg = pygame.image.load('fisher.png') #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
playerX = 150
playerY = 320
playerX_change = 0
playerY_change = 0
playerspeed = 3

# shells - Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
shell1 = pygame.image.load('shell1a.png')
shell2 = pygame.image.load('shell1b.png')
shell3 = pygame.image.load('shell1c.png')
shell4 = pygame.image.load('shell2a.png')
shell5 = pygame.image.load('shell2b.png')
shell6 = pygame.image.load('shell2c.png')
shell7 = pygame.image.load('shell3a.png')
shell8 = pygame.image.load('shell3b.png')
shell9 = pygame.image.load('shell3c.png')
shellImg = [shell1,shell2,shell3,shell4,shell5,shell6,shell7,shell8,shell9]
shelldir = (-0.01, 0.01)
shellwig = 5
shellX = []
shellY =  []
shellX_change = []
shellY_change = []
initshellX = []
initshellY = []
shellname = []
shellImgIndex = []  
NumOfShells = 0

def shellgen(x):
    for i in range(x):
        shellX.append(random.randint(16,769))
        shellY.append(random.randint(175,567))
        shellX_change.append(random.choice(shelldir))
        shellY_change.append(random.choice(shelldir))
        shellImgIndex.append(random.randint(0,8))
        initshellX.append(shellX[i])
        initshellY.append(shellY[i])
        screen.blit(shellImg[(shellImgIndex[i])], (shellX[i], shellY[i]))
def player(x, y):
    screen.blit(playerImg, (x, y))           

def isCollision(shellX,shellY,playerX,playerY):
    distance = math.sqrt((math.pow(shellX-playerX,2)) + (math.pow(shellY-playerY,2)))
    if distance <27:
        return True
    return False

# Game Loop - Infinite loop - 
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
    #while NumOfShells < 15:
    shellgen(15)
    for i in range(len(shellImgIndex)):
        shellX[i] += shellX_change[i]
        shellY[i] += shellY_change[i]
        if shellX[i] >= initshellX[i] + 5:
            shellX_change[i] -= 0.1
        elif shellX[i] <= initshellX[i] - 5:
            shellX_change[i] += 0.1
        elif shellY[i] >= initshellY[i] + 5:
            shellY_change[i] -= 0.1
        elif shellY[i] <= initshellY[i] - 5:
            shellY_change[i] += 0.1
        collision = isCollision(shellX[i],shellY[i],playerX,playerY)
        if collision:
            shellX[i] = random.randint(16,769)
            shellY[i] = random.randint(175,567)
    player(playerX, playerY)
    pygame.display.update() 