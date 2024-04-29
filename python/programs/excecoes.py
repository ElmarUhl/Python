try:
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    r = a/b
except Exception as erro:
    print('Erro, não foi possível fazer a operação')
    print(f'O problema foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Muito obrigado')