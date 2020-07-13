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

# player
playerImg = pygame.image.load('fisher.png') #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
playerX = 150
playerY = 320
playerX_change = 0
playerY_change = 0
playerspeed = 1
# net - Icons made by <a href="https://www.flaticon.com/free-icon/net_2764644" title="surang">surang</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
netImg = pygame.image.load('net.png')
netX = 720
netY = 45
catchImg = pygame.image.load('initLastCatch.png')
catchX = 720
catchY = 45

#background
background = pygame.image.load('riverbank.png')

# Music
mixer.music.load('music.wav')
mixer.music.play(-1)

# shells - Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
shelllist = ('a', 'b', 'c')
shelldir = (-0.01, 0.01)
shellX = []
shellY =  []
shellX_change = []
shellY_change = []
shellImg = []
shellnames = []
initshellX = []
initshellY = []
NumOfShells = 15
for i in range(NumOfShells):
    shellX.append(random.randint(16,769))
    shellY.append(random.randint(175,567))
    shellX_change.append(random.choice(shelldir))
    shellY_change.append(random.choice(shelldir))
    shellImg.append(pygame.image.load('shell'+str(random.randint(1,3))+random.choice(shelllist)+'.png'))
    initshellX.append(shellX[i])
    initshellY.append(shellY[i])
    

#Score
score_value = 0
font = pygame.font.Font('Organo.ttf', 22)
scoretextX = 10
scoretextY = 10
def show_score(x, y):
    score = font.render("Score " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
#Clock
clock_value = 10
clocktextX = 10
clocktextY = 40
def show_clock(x, y):
    clock = font.render("Timer "+ str(clock_value), True, (255, 255, 255))
    screen.blit(clock, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))   

def shell(x, y, i):
    screen.blit(shellImg[i], (x, y))

def net(x,y):
    screen.blit(netImg, (x, y))
    net_lable = font.render("Last Catch", True, (255, 255, 255))
    screen.blit(net_lable, (x - 55, y - 20))

def last_catch (x, y):
    screen.blit(catchImg, (x, y))

#collision detection equation
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
        # check for keystrokes
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
                
    # create some moving shells
    for i in range(NumOfShells):
        shell(shellX[i], shellY[i], i)
        shellX[i] += shellX_change[i]
        shellY[i] += shellY_change[i]
        if shellX[i] >= initshellX[i] + 5:
            shellX_change[i] -= 0.001
        elif shellX[i] <= initshellX[i] - 5:
            shellX_change[i] += 0.001
        elif shellY[i] >= initshellY[i] + 5:
            shellY_change[i] -= 0.001
        elif shellY[i] <= initshellY[i] - 5:
            shellY_change[i] += 0.001  
        collision = isCollision(shellX[i],shellY[i],playerX,playerY)
        if collision:
            splash_sound = mixer.Sound('splash.wav')
            splash_sound.play()
            score_value += 1
            shellX[i] = random.randint(16,769)
            initshellX[i] = shellX[i]
            shellY[i] = random.randint(175,567)
            initshellY[i] = shellY[i]
            catchImg = shellImg[i]
            last_catch(netX, netY)
            #print(pygame.surface.__name__(shellImg[i]) )
               
        

    player(playerX, playerY)
    net(netX, netY)
    last_catch(netX,netY)
    show_score(scoretextX, scoretextY)
    show_clock(clocktextX, clocktextY)
    
    pygame.display.update() 