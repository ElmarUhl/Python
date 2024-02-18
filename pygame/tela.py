import pygame
from pygame.locals import *
from sys import exit

# Initialize pygame
pygame.init()

# create the screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Jogo")

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.display.update()
