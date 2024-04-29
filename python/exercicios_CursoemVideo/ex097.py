def escreva(texto):
    c = len(texto) + 2
    print('~'*c)
    print('{:^{}}'.format(texto, c))
    print('~'*c)


# Programa principal    
texto = input('Digite o texto: ')
escreva(texto)
