import pygame
from pygame.locals import *
from sys import exit

pygame.init()

altura = 600
largura = 800
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')

relogio = pygame.time.Clock()

x = largura/2
y = altura/2

while True:
    tela.fill((0,0,0))
    relogio.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x -= 5
            if event.key == K_RIGHT:
                x += 5
            if event.key == K_UP:
                y -= 5
            if event.key == K_DOWN:
                y += 5
    
    pygame.draw.rect(tela, (255, 0, 0),(x, y, 10, 10))
    
            
    pygame.display.update()