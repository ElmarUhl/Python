count = 0
soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    count += 1
    soma += n

print('You input {} numbers and sum was {}'.format(count,soma))
