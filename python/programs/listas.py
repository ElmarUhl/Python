num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop(2)
print(num)
num.append(2)
print(num)
num.remove(2)
print(num)

valores = list()
for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    valores.append(n)

print(n)

b = valores # Cria uma ligação entre b e valores
b = valores[:] # cria uma copia dos valores
