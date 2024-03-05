import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Cobrinha')

relogio = pygame.time.Clock()

x_cobra = largura // 2
y_cobra = altura // 2

x_maca = randint(10, largura - 10)
y_maca = randint(10, altura - 10)

pontos = 0
fonte = pygame.font.SysFont('arial', 20, False, False)

tamanho_cobra = 100
morreu = False

velocidade = 2
x_controle = 2
y_controle = 0

music = pygame.mixer.music.load('evolution.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

som_colisao = pygame.mixer.Sound('smw_coin.wav')
som_colisao.set_volume(1.0)

lista_cobra = []
def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, 'green', (xey[0], xey[1], 10, 10))
        
def reiniciar():
    global pontos, tamanho_cobra, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    
    pontos = 0
    tamanho_cobra = 5
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(10, largura - 10)
    y_maca = randint(10, altura - 10)
    morreu = False

while True:
    relogio.tick(60)
    tela.fill('white')
    
    mensagem = 'Pontos {}'.format(pontos)
    texto_formatado = fonte.render(mensagem, True, 'black')

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle
            
    cobra = pygame.draw.rect(tela, (0,250,0), (x_cobra, y_cobra, 10, 10))
    maca = pygame.draw.rect(tela, 'red', (x_maca, y_maca, 10, 10))
            
    if cobra.colliderect(maca):
        x_maca = randint(10, largura - 10)
        y_maca = randint(10, altura - 10)
        pontos += 1
        som_colisao.play()
        tamanho_cobra += 1
        #velocidade += 1
    
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca) > 1:
        font2 = pygame.font.SysFont('arial', 20, False, False)
        mensagem2 = 'Game Over - Pressione r para jogar novamente'
        texto_formatado = font2.render(mensagem2, True, 'black')
        retTexto = texto_formatado.get_rect()
        
        morreu = True
        while morreu:
            tela.fill('white')
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
                        
            retTexto.center = (largura//2, altura//2)   
            tela.blit(texto_formatado, retTexto)
            
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
       
    if len(lista_cobra) > tamanho_cobra:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)
     
    tela.blit(texto_formatado, (10, 10))
    pygame.display.update()
    