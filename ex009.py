n = int(input('Digite um número: '))

print('Tabuada do {}.'.format(n))
i = 1
while i < 10:
    print('{} x {} = {}'.format(i, n, i*n))
    i += 1
