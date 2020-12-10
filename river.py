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
icon = pygame.image.load('data/rafting.png')
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load('data/fisher.png') #Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
playerX = 150
playerY = 320
playerX_change = 0
playerY_change = 0
playerspeed = 2.5
# net - Icons made by <a href="https://www.flaticon.com/free-icon/net_2764644" title="surang">surang</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
netImg = pygame.image.load('data/net.png')
netX = 720
netY = 45
# last caught shell
catchImg = pygame.image.load('data/initLastCatch.png')
catchX = 0
catchY = 0
#background
background = pygame.image.load('data/riverbank.png')
#menu
splash = pygame.image.load('data/title_screen.png')
# Music
mixer.music.load('data/music.wav')
mixer.music.play(-1)
# shells - Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
shelllist = ('a', 'b', 'c')
shellX = []
shellY =  []
shellX_change = []
shellImg = [pygame.image.load('data/shell1a.png'),pygame.image.load('data/shell2a.png'),pygame.image.load('data/shell3a.png'),pygame.image.load('data/shell1b.png'),pygame.image.load('data/shell2b.png'),pygame.image.load('data/shell3b.png'),pygame.image.load('data/shell1c.png'),pygame.image.load('data/shell2c.png'),pygame.image.load('data/shell3c.png'),]
shellnames = []
shellImgIndex = [0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8,0,1,2,3,4,5,6,7,8]
speed_list = ['0.1', '0.2', '0.05', '0.025', '0.3', '0.4']
NumOfShells = 45
catchImgIndex = 9
for i in range(NumOfShells):
    shellY.append(random.randint(175,567))
    shellX.append(random.randint(803,1500))
    shellX_change.append(random.choice(speed_list))
#Score
score_value = 0
highScore = 0
last_point = 0
font = pygame.font.Font('data/Organo.ttf', 22)
scoretextX = 10
scoretextY = 10
#Clock
timer = pygame.time.Clock()
currentTime = 0
gameEndTime = 0
highTime = 0
collisionTime = 0
penaltyTime = 0
clockTime = 0
clocktextX = 10
clocktextY = 40
#functions
def show_score(x, y):
    global highScore
    global score_value
    score = font.render("score " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    if score_value > 0:
        if highScore < score_value:
            highScore = score_value
    scoreRecord = font.render("high score " + str(highScore), True, (255, 255, 255))
    screen.blit(scoreRecord, (x + 125, y))
def resetGame():
    global score_value
    global catchImgIndex
    global clockTime
    global last_point
    global gameEndTime
    global netX
    global catchX
    global catchY
    score_value = 0
    last_point = 0
    gameEndTime = pygame.time.get_ticks()
    clockTime = 0
    catchImgIndex = 9
    catchX = 3000
    catchY = 3000
def score(shellImgIndex):
    global score_value
    global catchImgIndex
    global currentTime
    global last_point
    global gameEndTime
    doScoreLoop = False
    noGood = -1
    #shell legality check
    if catchImgIndex == 9:
        score_value += 1
        catchImgIndex = shellImgIndex
        last_point = 1
    elif catchImgIndex == 8:
        if shellImgIndex == 8 or shellImgIndex == 7 or shellImgIndex == 6 or shellImgIndex == 5 or shellImgIndex == 2:
            noGood = 1
        elif shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 3 or shellImgIndex == 4:
            noGood = 0
    elif catchImgIndex == 7:
        if shellImgIndex == 8 or shellImgIndex == 7 or shellImgIndex == 6 or shellImgIndex == 4 or shellImgIndex == 1:
            noGood = 1
        elif shellImgIndex == 0 or shellImgIndex == 2 or shellImgIndex == 5 or shellImgIndex == 3:
            noGood = 0
    elif catchImgIndex == 6:
        if shellImgIndex == 8 or shellImgIndex == 7 or shellImgIndex == 6 or shellImgIndex == 0 or shellImgIndex == 3:
            noGood = 1
        elif shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 4 or shellImgIndex == 5:
            noGood = 0
    elif catchImgIndex == 5:
        if shellImgIndex == 3 or shellImgIndex == 4 or shellImgIndex == 5 or shellImgIndex == 8 or shellImgIndex == 2:
            noGood = 1
        elif shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 6 or shellImgIndex == 7:
            noGood = 0
    elif catchImgIndex == 4:
        if shellImgIndex == 3 or shellImgIndex == 4 or shellImgIndex == 5 or shellImgIndex == 7 or shellImgIndex == 1:
            noGood = 1
        elif shellImgIndex == 0 or shellImgIndex == 2 or shellImgIndex == 6 or shellImgIndex == 8:
            noGood = 0
    elif catchImgIndex == 3:
        if shellImgIndex == 3 or shellImgIndex == 4 or shellImgIndex == 5 or shellImgIndex == 0 or shellImgIndex == 6:
            noGood = 1
        elif shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 7 or shellImgIndex == 8:
            noGood = 0
    elif catchImgIndex == 2:
        if shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 5 or shellImgIndex == 8:
            noGood = 1
        elif shellImgIndex == 3 or shellImgIndex == 4 or shellImgIndex == 6 or shellImgIndex == 7:
            noGood = 0
    elif catchImgIndex == 1:
        if shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 4 or shellImgIndex == 7:
            noGood = 1
        elif shellImgIndex == 3 or shellImgIndex == 5 or shellImgIndex == 6 or shellImgIndex == 8:
            noGood = 0
    elif catchImgIndex == 0:
        if shellImgIndex == 0 or shellImgIndex == 1 or shellImgIndex == 2 or shellImgIndex == 3 or shellImgIndex == 6:
            noGood = 1
        elif shellImgIndex == 4 or shellImgIndex == 5 or shellImgIndex == 7 or shellImgIndex == 8:
            noGood = 0
    if noGood == 1:
        resetGame()
    elif noGood == 0:
        catchImgIndex = shellImgIndex
        doScoreLoop = True
    #point accelerator
    if catchImgIndex < 9 and doScoreLoop:
        if ((currentTime - collisionTime)/1000) >= 5.1:
            score_value +=1
            last_point = 1
            startingPower = -1
        elif ((currentTime - collisionTime)/1000) >= 5:
            startingPower = 1
        elif ((currentTime - collisionTime)/1000) >= 3.333:
            startingPower = 2
        elif ((currentTime - collisionTime)/1000) >= 2.5:
            startingPower = 3
        elif ((currentTime - collisionTime)/1000) >= 2:
            startingPower = 4
        elif ((currentTime - collisionTime)/1000) >= 1.666:
             startingPower = 5
        elif ((currentTime - collisionTime)/1000) >= 1.428:
             startingPower = 6
        elif ((currentTime - collisionTime)/1000) >= 1.25:
            startingPower = 7
        elif ((currentTime - collisionTime)/1000) >= 1.11:
            startingPower = 8
        elif ((currentTime - collisionTime)/1000) < 1.11:            
            startingPower = 9
        for i in range (startingPower,-1,-1):
            power = 2**i
            next_power = 2**(i+1)
            if last_point >= power:
                score_value += next_power
                last_point = next_power
                break
def show_clock(x, y):
    global highTime
    global clockTime
    global score_value
    clockTime = int((currentTime - gameEndTime) / 1000)   
     
    if clockTime > 0:
        if highTime < clockTime:
            highTime = clockTime
    if score_value == 0:
        resetGame()
    timeRecord = font.render("high time "+ str(highTime), True, (255, 255, 255))
    screen.blit(timeRecord, (x + 125, y))
    clock = font.render("timer "+ str(clockTime), True, (255, 255, 255))
    screen.blit(clock, (x, y))
def player(x, y):
    screen.blit(playerImg, (x, y))   
def shell(x, y, i):
    screen.blit(shellImg[shellImgIndex[i]], (x, y))
def net(x,y):
    screen.blit(netImg, (x, y))
    net_lable = font.render("last catch", True, (255, 255, 255))
    screen.blit(net_lable, (x - 55, y - 20))
def last_catch (x, y):
    screen.blit(catchImg, (x, y))
def isCollision(shellX,shellY,playerX,playerY):
    distance = math.sqrt((math.pow(shellX-playerX,2)) + (math.pow(shellY-playerY,2))) #collision detection equation
    if distance <24:
        return True
    return False
########### Game Loop - Infinite loop ####################
menu = True 
running = True
while running:
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu = False
        screen.fill((0,0,0))
        screen.blit(splash,(0,0))
        pygame.display.update()

    screen.fill((204, 229, 255)) # rgb parameters
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# check for keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                menu = True
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
            splash_sound = mixer.Sound('data/splash.wav')
            splash_sound.play()
            shellY[i] = random.randint(175,567)
            shellX[i] = random.randint(803,1500)
            shellX_change[i] = random.choice(speed_list)
            catchImg = shellImg[shellImgIndex[i]]
            score(shellImgIndex[i])
            catchX = netX
            catchY = netY
            last_catch(catchX, catchY)
            collisionTime = pygame.time.get_ticks()
#time penalty
    if ((currentTime - collisionTime)/1000) >= 10 and score_value > 0:
            collisionTime = pygame.time.get_ticks()
            score_value -=1
            last_point = 1
    currentTime = pygame.time.get_ticks()
    player(playerX, playerY)
    net(netX, netY)
    last_catch(catchX, catchY)
    show_score(scoretextX, scoretextY)
    show_clock(clocktextX, clocktextY)
    pygame.display.update()
    timer.tick(120)