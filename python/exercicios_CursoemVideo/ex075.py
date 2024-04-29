n = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: '))) 

pares = 0
for i in n:
    if i % 2 == 0:
        pares += 1
        
print('O número 9 aparece {} vezes'.format(n.count(9)))
print(f'O número 3 aparece na posição {n.index(3)}')
print(f'A tupla contém {pares} numeros pares')
