def maior(*numeros):
    l = len(numeros)
    for i in range(0, l):
        if i == 0:
            maior = numeros[i]
        if numeros[i] > maior:
            maior = numeros[i]
    print(f'Foram dados {l} valores')
    print(f'O maior número da listagem é {maior}.')


# Programa principal
maior(1,3,4, 9, 23, 11, 2)
        
    