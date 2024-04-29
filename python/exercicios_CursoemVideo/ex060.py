from math import factorial

n = int(input('Digite um número: '))
# Resolvendo com a biblioteca
print('O fatorial do número é {}'.format(factorial(n)))

# Resolvendo com while
i = n
fatorial = 1
while i > 0:
    fatorial *= i
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    i -= 1
print('O fatorial do número {} é {}'.format(n, fatorial))

# Resolvendo com for
fatorial = 1
for i in range(1, n+1):
    fatorial *= i
print('O fatorial do número {} é {}'.format(n, fatorial))
