a0 = float(input('Digite o primeiro termo: '))
r = float(input('Digite a razão: '))

n = 0
while n < 10:
    print('{}'.format(a0 + n * r), end='')
    print(' - ' if n < 9 else '\n', end='')
    n += 1

continua = 1
while continua != 0:
    nTermos = int(input('Deseja ver mais termos? Se sim digite o número, se não digite 0: '))
    continua = nTermos
    i = 0
    while i < nTermos:
        print('{}'.format(a0 + n * r), end='')
        print(' - ' if i < nTermos-1 else '\n', end='')
        i += 1
        n += 1
        
        