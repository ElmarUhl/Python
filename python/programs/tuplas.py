lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')

print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[1:])
print(lanche[:2])
print(lanche[-4:-2])
print(lanche[-2:])
print(lanche[:-2])

for comida in lanche:
    print(comida)

for comida in range(0, len(lanche)):
    print(lanche[comida])
    
for pos, comida in enumerate(lanche):
    print(comida, pos)

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(8))
print(c.index(2,1))



