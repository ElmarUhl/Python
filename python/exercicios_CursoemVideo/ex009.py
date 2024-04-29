
n = int(input('Type a number: '))

print('Multiplication table of {}.'.format(n))
i = 1
while i < 10:
    print('{} x {} = {}'.format(i, n, i*n))
    i += 1
