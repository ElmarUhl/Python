vendedores = ["Marcus", "Amanda", "Ale", "Carol"]
vendas = [15, 20, 10, 30]

print(vendedores)
print(vendas)

# com enumerate
print('Listagem com enumerate')
print('-'*30)
for i, vendedor in enumerate(vendedores):
    print(f'{i} - {vendedor} - {vendas[i]}')

print()

# com zip
print('Listagem com zip')
print('-'*30)
for vendedor, vendas in zip(vendedores, vendas):
    print(f'{vendedor} - {vendas}')
