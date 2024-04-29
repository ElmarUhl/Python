def leiaDinheiro(texto):
    n = input(f'{texto}').strip().replace(',','.')
    while n.isalpha() or n == '':
        n = input('Valor inválido digite novamente: ')
        
    return float(n)
