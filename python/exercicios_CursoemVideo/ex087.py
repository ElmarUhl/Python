matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0, 3):
    for ii in range(0, 3):
        matriz[i][ii] = int(input('Digite um valor: '))

print(matriz)

soma_pares = 0
soma_coluna = 0
for i in range(0, 3):
    for ii in range(0, 3):
        if matriz[i][ii] % 2 == 0:
            soma_pares += matriz[i][ii]
        
        if ii == 2:
            soma_coluna += matriz[i][ii]

print(f'A soma dos números pares é {soma_pares}')
print(f'A soma dos valores da 3a. coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

