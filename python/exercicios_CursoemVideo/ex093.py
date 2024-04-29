cadastro = dict()
gols = []

cadastro['nome'] = input('Digite o nome do jogador: ')
cadastro['no. partidas'] = int(input('Digite o número de partidas: '))
for partida in range(0, cadastro['no. partidas']):
    gols.append(int(input(f'Digite o número de gols da partida: ')))
cadastro['gols'] = gols

soma = 0
for i in range(0, len(cadastro['gols'])):
    soma += cadastro['gols'][i]
    
cadastro['total de gols'] = soma

print(cadastro)
for k,v in cadastro.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {cadastro["nome"]} jogou {cadastro["no. partidas"]} partidas')

for k, v in enumerate(cadastro['gols']):
    print(f'Na partida {k+1} o jogador fez {v} gols')
    
print(f'Foram no total {cadastro["total de gols"]} gols.')
