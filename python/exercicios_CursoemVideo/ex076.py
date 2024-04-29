lista = ('Novalgina', '10,50', 'Coleira', '5,30', 'Corrente', '2,00')

for i in range(0, len(lista), 2):
    produto = lista[i]
    preco = lista[i + 1]

    print(f'{produto} {preco}')
