import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('evolution.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(1.0)

relogio = pygame.time.Clock()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

fonte = pygame.font.SysFont('arial', 20, False, False)
pontos = 0

x = largura/2
y = altura/2

x2 = randint(10, largura - 10)
y2 = randint(10, altura-10)

while True:
    tela.fill((0,0,0))
    relogio.tick(60)

    mensagem = 'Pontos {}'.format(pontos)
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    retangulo1 = pygame.draw.rect(tela, (255,0,0), (x, y, 10, 10))
    retangulo2 = pygame.draw.rect(tela, (0,255,0), (x2, y2, 10, 10))

    if pygame.key.get_pressed()[K_LEFT]:
        x -= 2
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 2
    if pygame.key.get_pressed()[K_UP]:
        y -= 2
    if pygame.key.get_pressed()[K_DOWN]:
        y += 2
        
    if retangulo1.colliderect(retangulo2):
        x2 = randint(10, largura - 10)
        y2 = randint(10, altura - 10)
        pontos += 1
        barulho_colisao.play()

    tela.blit(texto_formatado, (10,10))
    pygame.display.update()
