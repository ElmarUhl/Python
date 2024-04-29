a = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA:'))

i = 0
while i < 10:
    an = a + i * r
    print('{}'.format(an), end='')
    print(' - ' if i < 9 else ' \n', end='')
    i += 1
    