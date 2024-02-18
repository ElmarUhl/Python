import math

angulo = float(input('Digite o valor do ângulo: '))
radianos = math.radians(angulo)

seno = math.sin(radianos)
coseno = math.cos(radianos)
tangente = math.tan(radianos)

print('O valor em radianos do ângulo {} é {}, seu seno é {}, o coseno é {} e a tangente é {}.'.format(angulo, radianos, seno, coseno, tangente))