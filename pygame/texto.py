import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

relogio = pygame.time.Clock()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))

fonte = pygame.font.SysFont('arial', 20, True, True)
#pygame.font.get_fonts()
pontos = 0

x = largura/2
y = altura/2

x2 = randint(10, largura - 10)
y2 = randint(10, altura - 10)

while True:
    tela.fill((0,0,0))
    relogio.tick(60)
    
    mensagem = 'Pontos {}'.format(pontos)
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

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

    retangulo1 = pygame.draw.rect(tela, (255,0, 0),(x, y, 10, 10))
    retangulo2 = pygame.draw.rect(tela, (0,255,0), (x2, y2, 10, 10))
    
    if retangulo1.colliderect(retangulo2):
        x2 = randint(10, largura -10)
        y2 = randint(10, altura - 10)
        pontos += 1

    tela.blit(texto_formatado, (10,10))
    pygame.display.update()
