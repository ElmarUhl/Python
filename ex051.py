
a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for n in range(0, 10):
    pa = a + n * r
    print(pa, end=' ')
    
print('')
