from random import randint

lista = ['pedra', 'papel', 'tesoura']

escolha = input('Escolha entre {}: '.format(lista))
computador = lista[randint(0,2)]

print('O computador escolheu {}'.format(computador))

if escolha == 'pedra' and computador == 'tesoura':
    print('Você ganhou')
elif escolha == 'papel' and computador == 'pedra':
    print('Você ganhou')
elif escolha == 'tesoura' and computador == 'papel':
    print('Você ganhou')
elif escolha == computador:
    print('Empate')
else:
    print('O computador ganhou')
