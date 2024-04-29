opcao = ''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

while opcao != 5:
    
    opcao = int(input("""Escolha uma opção
    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa\n"""
    ))
    
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto de {} e {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 == n2:
            print('Os números são iguais a {}'.format(n1))        
        elif n1 > n2:
            print('O número {} é o maior'.format(n1))
        else:
            print('O número {} é o maior'.format(n2))
    elif opcao == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
            
