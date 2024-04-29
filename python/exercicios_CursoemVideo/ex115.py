def cadastro():
    print('-'*40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-'*40)
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: '))
    f = open('cadastro.txt', 'a')
    f.write(f'{nome} {idade}\n')
    f.close()


def leitura():
    f = open('cadastro.txt', 'r')
    print('-'*40)
    print('{:^40}'.format('PESSOAS CADASTRADAS'))
    print('-'*40)
    #print(f.read())
    for i in f:
        x = i.split()
        n = len(x)
        nome = ''
        idade = ''
        for ii in range(0,n):
            if ii == n-1:
                idade = x[ii]
            else:
                nome += x[ii] + ' '
        nome = nome.strip()
        print(f'{nome:.<30} {idade} anos')
    print('-'*40)
    f.close()


# Programa principal    
while True:
    print('-'*40)
    print('{:^40}'.format('MENU PRINCIPAL'))
    print('-'*40)
    print('1 - Mostrar cadastro de pessoas')
    print('2 - Cadastrar pessoas')
    print('3 - Sair')
    print('-'*40)
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        leitura()
    elif opcao == 2:
        cadastro()
    elif opcao == 3:
        break
    else:
        print('Opção inválida')
