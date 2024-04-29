
n = int(input('Digite o número de termos da sequência de Fibonacci: '))

nFirst = 0
nSecond = 1

print('Sequência de Fibonacci')
print('{} - {} - '.format(nFirst, nSecond), end='')

i = 0
while i < n:
    temp = nFirst + nSecond
    print ('{}'.format(temp), end='')
    print(' - ' if i < n-1 else '\n', end='')

    nFirst = nSecond
    nSecond = temp
    
    i += 1
    
