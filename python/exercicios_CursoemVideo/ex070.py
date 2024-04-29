continua = 'S'
soma = 0
count = 0
preco = 0
menor = 0
nome_menor = 0

while continua == 'S':
    continua = ' '
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))

    soma += preco
    
    if preco > 1000:
        count += 1

    if menor == 0:
        menor == preco
        nome_menor = produto
        
    if preco < menor:
        menor = preco
        nome_menor == produto

    while continua not in 'SN':
        continua = input('Deseja continuar [S/N]: ').strip().upper()

print('O total gasto foi R$ {:.2f}'.format(soma))
print('São {} produtos com valor acima de R$ 1000,00'.format(count))
print('O produto mais barato é {}'.format(nome_menor))
