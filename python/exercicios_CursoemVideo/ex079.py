numeros = []

print('Digite N para terminar')
while True:
    n = input('Digte um valor: ').strip().upper()

    if n == 'N':
        break

    if not n in numeros:
        numeros.append(int(n))

    print(f'O valores são {sorted(numeros)}')
