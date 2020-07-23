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
playerspeed = 3
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
shellX = []
shellY =  []
shellX_change = []
shellImg = [pygame.image.load('shell1a.png'),pygame.image.load('shell2a.png'),pygame.image.load('shell3a.png'),pygame.image.load('shell1b.png'),pygame.image.load('shell2b.png'),pygame.image.load('shell3b.png'),pygame.image.load('shell1c.png'),pygame.image.load('shell2c.png'),pygame.image.load('shell3c.png'),]
shellnames = []
shellImgIndex = [0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8]
speed_list = ['0.1', '0.2', '0.05', '0.025', '0.3', '0.4']
NumOfShells = 54
catchImgIndex = 9
for i in range(NumOfShells):
    shellY.append(random.randint(175,567))
    shellX.append(random.randint(803,1500))
    shellX_change.append(random.choice(speed_list))

#Score
score_value = 0
font = pygame.font.Font('Organo.ttf', 22)
scoretextX = 10
scoretextY = 10
def show_score(x, y):
    score = font.render("Score " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def score(shellImgIndex):
    global score_value
    global catchImgIndex
    global currentTime
    if catchImgIndex == 9:
        score_value += 1
        catchImgIndex = shellImgIndex
    elif catchImgIndex == 8:
        if shellImgIndex == 8 or shellImgIndex == 7 or shellImgIndex == 6 or shellImgIndex == 5 or shellImgIndex == 2:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 3 or shellImgIndex == 4:
            score_value += 1
            catchImgIndex = shellImgIndex
    elif catchImgIndex == 7:
        if shellImgIndex == 8 or shellImgIndex == 7 or shellImgIndex == 6 or shellImgIndex == 4 or shellImgIndex == 1:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 0 or shellImgIndex == 2 or shellImgIndex == 5 or shellImgIndex == 3:
            score_value += 1
            catchImgIndex = shellImgIndex
    elif catchImgIndex == 6:
        if shellImgIndex == 8 or shellImgIndex == 7 or shellImgIndex == 6 or shellImgIndex == 0 or shellImgIndex == 3:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 4 or shellImgIndex == 5:
            score_value += 1
            catchImgIndex = shellImgIndex
    elif catchImgIndex == 5:
        if shellImgIndex == 3 or shellImgIndex == 4 or shellImgIndex == 5 or shellImgIndex == 8 or shellImgIndex == 2:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 6 or shellImgIndex == 7:
            score_value += 1
            catchImgIndex = shellImgIndex
    elif catchImgIndex == 4:
        if shellImgIndex == 3 or shellImgIndex == 4 or shellImgIndex == 5 or shellImgIndex == 7 or shellImgIndex == 1:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 0 or shellImgIndex == 2 or shellImgIndex == 6 or shellImgIndex == 8:
            score_value += 1
            catchImgIndex = shellImgIndex
    elif catchImgIndex == 3:
        if shellImgIndex == 3 or shellImgIndex == 4 or shellImgIndex == 5 or shellImgIndex == 0 or shellImgIndex == 6:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 7 or shellImgIndex == 8:
            score_value += 1
            catchImgIndex = shellImgIndex
    elif catchImgIndex == 2:
        if shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 5 or shellImgIndex == 8:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 3 or shellImgIndex == 4 or shellImgIndex == 6 or shellImgIndex == 7:
            score_value += 1
            catchImgIndex = shellImgIndex
    elif catchImgIndex == 1:
        if shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 4 or shellImgIndex == 7:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 3 or shellImgIndex == 5 or shellImgIndex == 6 or shellImgIndex == 8:
            score_value += 1
            catchImgIndex = shellImgIndex
    elif catchImgIndex == 0:
        if shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 3 or shellImgIndex == 6:
            score_value = 0
            currentTime = 0
            catchImgIndex = 9
        elif shellImgIndex == 4 or shellImgIndex == 5 or shellImgIndex == 7 or shellImgIndex == 8:
            score_value += 1
            catchImgIndex = shellImgIndex

#Clock
timer = pygame.time.Clock()
currentTime = 0
collisionTime = 0
clocktextX = 10
clocktextY = 40

def show_clock(x, y):
    clockTime = int(((currentTime - collisionTime)/1000))
    clock = font.render("Timer "+ str(clockTime), True, (255, 255, 255))
    screen.blit(clock, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))   

def shell(x, y, i):
    screen.blit(shellImg[shellImgIndex[i]], (x, y))

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
        shellX[i]-= float(shellX_change[i])
        collision = isCollision(shellX[i],shellY[i],playerX,playerY)
        if shellX[i] <= 0:
            shellX[i] = random.randint(803,1500)
        if collision:
            splash_sound = mixer.Sound('splash.wav')
            splash_sound.play()
            shellY[i] = random.randint(175,567)
            shellX[i] = random.randint(803,1500)
            shellX_change[i] = random.choice(speed_list)
            catchImg = shellImg[shellImgIndex[i]]
            score(shellImgIndex[i])
            last_catch(netX, netY)
            collisionTime = pygame.time.get_ticks()
     
    currentTime = pygame.time.get_ticks()
    player(playerX, playerY)
    net(netX, netY)
    last_catch(netX,netY)
    show_score(scoretextX, scoretextY)
    show_clock(clocktextX, clocktextY)
    pygame.display.update()
    timer.tick(120)