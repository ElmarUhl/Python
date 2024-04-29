# Definição de função
def titulo(txt):
    print('-'*60)
    print(f'{txt:^60}')
    print('-'*60)
# Chama a função
titulo('Aprenda Python')

# Função com parâmetros
def soma(a, b):
    c = a + b
    print(c)
soma(3, 7)
soma(4,5)
soma(b=3, a=2)

# Função com empacotamento
def soma2(*valores):
    soma = 0
    for num in valores:
        soma += num
    print(soma)
soma2(3, 4, 5, 9)

def contador(*numeros):
    tam = len(numeros)
    print(f'A função contador recebeu {tam} parâmetros')
contador(2,1,3)

# Uso de docstrings
def contador2(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    param i: início da contagem
    param f: fim da contagem
    param p: passo da contagem
    return: sem valor de retornoq
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')
contador2(2, 20, 3)
#help(contador2)

# Parâmetros opcionais
def somar(a=0, b=0, c=0):
    print(f'{a} {b} {c}')
somar(1, 2, 3)
somar(1,2)

# Escopo de variável
def teste():
    # Variáveis locais
    x = 8
    n1 = 4
    print(f'Na na função teste, n vale {n}')
    print(f'N função teste, x vale {x}')
    print(f'N1 dentro vale {n1}')

# Programa Principal
# Variáveis globais
n = 2
n1 = 2
print(f'No programa principal, n vale {n}')
teste()
#print(f'No programa principal x vale {x}')
print(f'N1 fora vale {n1}')

def teste2(b):
    global a
    a = 8
    b = 3
    c = 4
    print(f'A dentro vale {a}')
    print(f'b vale {b}')
    print(f'c vale {c}')

a = 5
teste2(a)
print(f'A fora vale {a}')

# Valores de retorno
def somar2(a, b):
    s = a + b
    return s
r1 = somar2(3, 4)
print(r1)
