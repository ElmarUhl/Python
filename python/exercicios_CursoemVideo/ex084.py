dados = list()
pessoas = list()

#print(f'Digite os dados de nome e peso, caso queira terminar digite N/n')
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    op = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if op == 'N':
        break

print(pessoas)
print(f'O número de pessoas cadastradas é {len(pessoas)}')

maior = menor = pessoas[0][1]
for i in pessoas:
    if maior < i[1]:
        maior = i[1]
    if menor > i[1]:
        menor = i[1]

print('O maior peso é {} kg de '.format(maior), end='')
for i in pessoas:
    if i[1] == maior:
        print(f'{i[0]}, ', end='')

print()
print('O menor peso é {} kg de '.format(menor), end='')
for i in pessoas:
    if i[1] == menor:
        print(f'{i[0]}, ', end='')

print()
