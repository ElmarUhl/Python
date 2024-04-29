from random import randint

numero = list()

def sorteia():
    for i in range(0, 5):
        numero.append(randint(1,100))
    print(f'Os números sorteados foram {numero}')
    
def somaPar():
    soma = 0
    for i in numero:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos valores pares é {soma}')
    
sorteia()
somaPar()
