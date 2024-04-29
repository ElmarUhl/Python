from random import randint

count = 0

continua = 1
venceu = 0

print('EVEN OR ODD GAME\n' + '{}'.format('-'*40))

while continua:
    option = input('Chose even or odd: ').strip().upper()[0]
    soma = 0

    computer = randint(0, 10)
    man = int(input('\nType a number: '))
    soma = computer + man

    print('\nThe computer chose {}'.format(computer))
    print('You chose {}'.format(man))
    print('Result is {}\n'.format(soma))
    
    if option == 'E':
        if not soma % 2:
            print('Você venceu!')
            venceu +=1
        else:
            print('Você perdeu!')
            continua = 0
    else:
        if not soma % 2:
            print('Você perdeu!')
            continua = 0
        else:
            print('Você venceu!')
            venceu += 1

print('Você venceu {} vezes'.format(venceu))