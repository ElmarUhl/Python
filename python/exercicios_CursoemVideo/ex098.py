from time import sleep

def contador(inicio, fim, passo):
    if inicio != fim and passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo *= -1
    if passo > 0:
        incremento = 1
    else:
        incremento = -1
    for i in  range(inicio, fim+incremento, passo):
        print(f'{i}', end=' ', flush=True)
        sleep(1)
    print()

# Programa principal
print('Conta de 1 a 10')
contador(1, 10, 1)
print('Contagem de 10 a 0')
contador(10,0, -1)

inicio = int(input('Digite o valor de início da contagem: '))
fim = int(input('Digite o valor do final da contagem: '))
passo = int(input('Digite o valor dos passos da contagem: '))

print(f'Contagem personalizada')
contador(inicio, fim, passo)
