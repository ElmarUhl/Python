number = []

for i in range(0, 5):
    n = int(input('Digite um valor: '))
    print(i)
    if i == 0:
        number.append(n)
        print('Adicionando ao início da fila')
    elif n > number[len(number)-1]:
        number.append(n)
        print('Adicionando no final da fila')
    else:
        pos = 0
        while pos < len(number):
            if n < number[pos]:
                number.insert(pos, n)
                print(f'Adicionando na posição {pos}')
                break
            pos += 1

print(number)