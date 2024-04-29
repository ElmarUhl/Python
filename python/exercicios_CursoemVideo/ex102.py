def fatorial(n,show=False):
    """
    -> Calcula o fatorial do número
    n param: número a ser calculado o fatorial
    show param: True ou False para mostrar os termos de cálculo do fatorial
    return: sem valor de retorno
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(f'{i}', end='')
            print(' x ' if i > 1 else ' = ', end='')
    print(f'{f}', end='')
    print()
  
fatorial(4,True)