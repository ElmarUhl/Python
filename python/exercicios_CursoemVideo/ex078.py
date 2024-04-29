numeros = list()

for i in range(0, 5):
    n = int(input('Digite um valor: '))
    numeros.append(n)
    
print(f'Você digitou {numeros}')
print(f'O menor valor foi {min(numeros)} na posição {numeros.index(min(numeros))}')
print(f'O maior valor foi {max(numeros)} na posição {numeros.index(max(numeros))}')
