def area(comprimento, largura):
    print('A área do terreno {}x{} é de {} m²'.format(comprimento, largura, comprimento*largura))

# Program principal
print('{:^50}'.format('Controle de Terreno'))
print('-'*50)
comprimento = float(input('LARGURA (m): '))
largura = float(input('COMPRIMENTO (m): '))
area(comprimento, largura)
