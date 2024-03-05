soma = 0
nomeVelho = ''
nMulheres = 0

maximo = 0

for c in range(0, 4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M para masculino e F para feminino): ')

    if idade > maximo and sexo == 'M':
        nomeVelho = nome
        maximo = idade
    
    soma += idade
    
    if idade < 20 and sexo == 'F':
        nMulheres += 1
        
print('O homem mais velhor é {}'.format(nomeVelho))
print('A média de idade é {}'.format(soma/4))
print('O número de mulheres com idade abaixo de 20 anos é {}'.format(nMulheres))
