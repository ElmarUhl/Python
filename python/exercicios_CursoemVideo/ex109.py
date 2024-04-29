import moeda2

p = float(input('Digite o preço: '))
valor = float(input('Digite o valor a aumentar ou diminuir: '))

print(f'O valor aumentado é {moeda2.aumentar(p,valor, True)} e o diminuído é {moeda2.diminuir(p,valor, True)}')
print(f'O valor aumentado é {moeda2.aumentar(p,valor)} e o diminuído é {moeda2.diminuir(p,valor)}')
print(f'O dobro do valor é {moeda2.dobro(p,True)} e a metade é {moeda2.metade(p,True)}')
print(f'O dobro do valor é {moeda2.dobro(p)} e a metade é {moeda2.metade(p)}')
