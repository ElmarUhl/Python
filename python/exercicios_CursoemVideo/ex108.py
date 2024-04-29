from moeda import *

p = float(input('Digite o valor: '))
valor = float(input('Digite o valor a aumentar ou diminuir: '))

print(f'O valor aumentado é {moeda(aumentar(p, valor))} e diminuido é {moeda(diminuir(p,valor))}')
print(f'O dobro é {moeda(dobro(p))} e a metade é {moeda(metade(p))}')
