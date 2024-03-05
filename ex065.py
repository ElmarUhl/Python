
continuar = 'SIM'
soma = maior = menor = contador = 0

while continuar == 'SIM':
    n = int(input('Digite um número: '))
    
    if contador == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
            
    soma += n
    contador += 1
        
    continuar = input('Deseja continuar? (sim ou não): ').strip().upper()
    
print('A média do valores foi {}, sendo o menor {} e o maior {}.'.format(soma/contador, menor, maior))
