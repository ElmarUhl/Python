# Normalização de caracteres
import numpy

name = 'curso de Deep Learning do Código Logo'
lista = list(name)

for i in lista:
    num = ord(i)/255
    print(f'{i} = {num}')
    