# Soma dos números entre 1 e 500 que são ímpares e múltiplos de 3

soma = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            soma += c
            
print(soma)

soma = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma += c

print(soma)

