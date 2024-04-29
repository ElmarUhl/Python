from random import randint

jogos = []
jogo = []

n = int(input('Digite o número de jogos a serem gerados: '))

for i in range(0, n):
    for ii in range(0, 6):
        n = randint(1, 60)
        while n in jogo: # Evita números duplicados
            n = randint(1, 60)
        jogo.append(n)
    jogos.append(jogo[:])
    jogo.clear()
    
print('Listagem de jogos gerados')
print('-'*30)
print(jogos)
    