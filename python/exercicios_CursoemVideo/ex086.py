matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0, 3):
    for ii in range(0, 3):
        matriz[i][ii] = int(input('Digite um valor: '))

for i in range(0, 3):
    for ii in range(0, 3):
        print(f'{[matriz[i][ii]]}', end='')
    print()
    