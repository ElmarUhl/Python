from moeda import *

p = float(input('Digite o preço da mercadoria em R$: '))
valor = float(input('Digite o valor de acréscimo ou decréscimo: '))
print('O novo valor acrescido é {}'.format(aumentar(p,valor)))
print('O novo valor com redução é {}'.format(diminuir(p,valor)))
print(f'O dobro do valor do produto é {dobro(p)}')
print(f'A metade do valor do produto é {metade(p)}')
