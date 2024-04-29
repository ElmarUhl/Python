numeros = []
pares = []
impares = []

while True:
    n = input('Digite um valor: ').strip().upper()

    if n == 'N':
        break
    
    numeros.append(int(n))

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
    
print(f'O números digitados foram {numeros}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')
