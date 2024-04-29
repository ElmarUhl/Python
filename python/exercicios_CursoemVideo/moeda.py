def aumentar(valor, valor2):
    return valor + valor2

def diminuir(valor, valor2):
    return valor - valor2

def dobro(valor):
    return 2*valor

def metade(valor):
    return valor/2

def moeda(valor):
    n  = 'R$ {:.2f}'.format(valor).replace('.',',')
    return(n)
