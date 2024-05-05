import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 800
altura = 400
tela = pygame.display.set_mode((largura,altura))

relogio = pygame.time.Clock()

x = largura/2
y = altura/2

x_retangulo = randint(10, largura-10)
y_retangulo = randint(10, altura-10)

while True:
    tela.fill((0,0,0))
    relogio.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_LEFT]:
        x -= 2
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 2
    if pygame.key.get_pressed()[K_UP]:
        y -= 2
    if pygame.key.get_pressed()[K_DOWN]:
        y += 2

    retangulo1 = pygame.draw.rect(tela,(0,0,255),(x,y,10,10))
    retangulo2 = pygame.draw.rect(tela,(0,255,0),(x_retangulo,y_retangulo,10,10))
    
    if retangulo1.colliderect(retangulo2):
        x_retangulo = randint(10, largura - 10)
        y_retangulo = randint(10, altura - 10)
            
    pygame.display.update()
