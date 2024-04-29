import math

c1 = float(input('Type the value length of right triangle side: '))
c2 = float(input('Type length of another side: '))

hypotenuse = math.sqrt(c1**2 + c2**2)

print('The length of hypotenuse is {}'.format(hypotenuse))

print('The length of hypotenuse is {}'.format(math.hypot(c1,c2)))
