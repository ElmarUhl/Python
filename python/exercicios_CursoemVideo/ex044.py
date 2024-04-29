preco = float(input('Digite o preço do produto: '))
condicao = input('Digite a condição de pagamento (`a vista, cartão, 2x, 3x ou mais):').strip().upper()

if condicao == 'À VISTA':
    print('O valor a ser pago é R$ {:.2f}'.format(preco - 0.10*preco))
elif condicao == 'CARTÃO':
    print('O valor a ser pago é R$ {:.2f}'.format(preco - 0.05*preco))
elif condicao == '2X':
    print('O valor a ser pago é R$ {:.2f}'.format(preco))
else:
    print('O valor a ser pago é R$ {:.2f}'.format(preco + 0.20*preco))
