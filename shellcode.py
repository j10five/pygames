import pygame
import random
import math
import time
from pygame import mixer
#initialize pygame module
pygame.init() 
screen = pygame.display.set_mode((800, 600)) 
background = pygame.image.load('riverbank.png')
NumOfShells = 0

def shellgen(x):
   for i in range(x):
      global NumOfShells 
      NumOfShells += 1
      print(NumOfShells)

# Game Loop - Infinite loop - 
running = True
while running:
    screen.fill((204, 229, 255)) # rgb parameters
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # initialize some shells
        for i in range(2):
            shellgen(2)
    print(NumOfShells)
    pygame.display.update() 