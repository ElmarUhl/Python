numero = 0
contador = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        soma += numero
        contador += 1
    
print('Você digitou {} números e sua soma é {}'.format(contador, soma)) 
 