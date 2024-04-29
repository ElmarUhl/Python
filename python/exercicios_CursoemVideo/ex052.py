
n = int(input('Digite um número: '))

primo = True

for i in range(n-1, 1, -1):
    if n % i == 0:
        print('O número é divisível por {}'.format(i))
        primo = False

if primo:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))
