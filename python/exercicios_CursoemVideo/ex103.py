def ficha(nome='', gols=''):
    if nome == '':
        nome = 'desconhecido'
    if gols.isdigit():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} marcou {gols} gols.')

n = input('Digite o nome do jogador: ')
g = input('Digite o número ')
ficha(n, g)
