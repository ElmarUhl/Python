numeros = [[],[]]

for i in range(0, 7):
    number = int(input(f'Digite o {i} valor: '))
    if number % 2 == 0:
        numeros[0].append(number)
    else:
        numeros[1].append(number)

numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são {numeros[0]}')
print(f'Os números ímpares são {numeros[1]}')
