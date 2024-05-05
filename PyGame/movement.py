import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 600
largura = 800

tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

x = largura/2
y = 0

while True:
    relogio.tick(60)
    
    tela.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.draw.rect(tela,(255,0,0),(x,y,50,50))
    if y >= altura:
        y = 0
        x = largura/2
    y += 5
    
    pygame.display.update()
            
            
        