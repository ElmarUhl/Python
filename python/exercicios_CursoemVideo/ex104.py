def leiaint(n):
    while not n.isnumeric():
        n = input('Valor inválido digite novamente: ')
    print(f'O valor é numérico e é {n}')

# Programa principal
leiaint(input('Digite um número: '))
