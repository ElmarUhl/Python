numeros = []

while True:
    n = input('Digite um valor: ').strip().upper()
    
    if n == 'N':
        break
    
    numeros.append(int(n))

print(numeros)
print(f'Foram digitados {len(numeros)}')
print(f'A lista é {sorted(numeros, reverse=True)}')

if int(5) in numeros:
    print('5 está na lista')
else:
    print('5 não está na lista')
