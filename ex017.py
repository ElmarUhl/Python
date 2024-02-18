from math import sqrt

c1 = float(input('Digite o valor de um lado do triângulo retângulo: '))
c2 = float(input('Digite o valor de outro lado do triângulo retângulo: '))

hipotenusa = sqrt(c1**2 + c2**2)

print('A medida da hipotenusa é {}'.format(hipotenusa))
