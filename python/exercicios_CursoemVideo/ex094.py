lista = list()

while True:
    nome = input('Digite o nome: ')
    while True:
        sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
        if sexo in 'MF':
            break
        print('Valor inválido digite somente M ou F')
    idade = int(input('Digite a idade: '))
    cadastro = dict()
    cadastro['nome'] = nome
    cadastro['sexo'] = sexo
    cadastro['idade'] = idade

    lista.append(cadastro)
    
    while True:
        option = input('Deseja adicionar mais cadastros? [S/N] ').strip().upper()[0]
        if option in 'SN':
            break
        print('Valor inválido, digite S ou N')
        
    if option == 'N':
        break

n_cadastros = len(lista)
print('Foram cadastradas {} pessoas.'.format(n_cadastros))

soma = 0
for i in lista:
    soma += i['idade']
media = soma/n_cadastros
print(f'A média de idade é {media}.')

mulheres = []
for i in lista:
    if i['sexo'] == 'F':
        mulheres.append(i['nome'])
print('As mulheres na lista são ', end='')
for i in mulheres:
    print(i, end=' ')
print()

velhos = []
for i in lista:
    if i['idade'] > media:
        velhos.append(i['nome'])
print(f'As pessoas com idade acima da média são {velhos}')
