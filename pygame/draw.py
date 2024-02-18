import pygame
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((800,600))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.draw.rect(tela, (255,0,0), (400,300,50,50))        
    pygame.draw.circle(tela, (0,255,0), (100, 100), 10)
    pygame.draw.line(tela,(0,0,255),(200,500),(450, 400), 2)
            
            
    pygame.display.update()