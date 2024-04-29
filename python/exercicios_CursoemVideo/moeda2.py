def aumentar(valor, valor2, format=False):
    retorna = valor + valor2
    if format:
        return moeda(retorna)
    else:
        return retorna
    
def diminuir(valor, valor2, format=False):
    retorna = valor - valor2
    if format:
        return moeda(retorna)
    else:
        return retorna

def dobro(valor, format=False):
    retorna = 2*valor
    if format:
        return moeda(retorna)
    else:
        return retorna

def metade(valor, format=False):
    retorna = valor/2
    if format:
        return moeda(retorna)
    else:
        return retorna

def moeda(valor):
    n  = 'R$ {:.2f}'.format(valor).replace('.',',')
    return(n)
    
def resumo(p):
    print('-'*40)
    print('{:^40}'.format('Preço Analisado'))
    print('-'*40)
    print(f'Preço analisado \t{moeda(p)}')
    print(f'Dobro do preço  \t{dobro(p,True)}')
    print(f'Metade do preço \t{metade(p,True)}')
    print(f'80% de aumento  \t{aumentar(p,0.8*p,True)}')
    print(f'35% de redução  \t{diminuir(p,0.35*p,True)}')
    print('-'*40)

