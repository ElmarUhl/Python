lista = list()

while True:
    cadastro = dict()
    gols = []
    nome = input('Digite o nome do jogador: ')
    partidas = int(input('Digite o número de partidas: '))
    cadastro['nome'] = nome
    cadastro['no. partidas'] = partidas
    for partida in range(0, partidas):
        n_gols = int(input(f'Digite o número de gols da partida {partida+1}: '))
        gols.append(n_gols)
    cadastro['gols'] = gols

    soma = 0
    for i in range(0, len(cadastro['gols'])):
        soma += cadastro['gols'][i]
    cadastro['total de gols'] = soma
    
    lista.append(cadastro)
    
    option = input('Deseja inserir mais cadastros? [S/N]').strip().upper()[0]
    if option == 'N':
        break

while True:
    option = input('Deseja ver dados de um jogador? [Nome/N]')
    for i in lista:
        if i['nome'] == option:
            print(i)
    if option in 'Nn':
        break    
    
print(lista)
