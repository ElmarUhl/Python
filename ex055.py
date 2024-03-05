maior = 0
menor = 500

for c in range(0, 5):
    n = int(input('Digite o peso em kg: '))
    if n > maior:
        maior = n
    
    if n < menor:
        menor = n
        
print('O maior peso foi {} e o menor foi {}'.format(maior, menor))
