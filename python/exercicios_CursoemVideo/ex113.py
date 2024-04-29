def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print('Erro! Valor inválido')
        except (KeyboardInterrupt):
            print('Entrada interrompida pelo usuário')
            return 0
        else:
            print(f'O valor é numérico e é {n}')
            return 0

def leiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError, TypeError):
            print('Erro! Valor inválido.')
            pass
        except (KeyboardInterrupt):
            print('Entrada interrompida pelo usuário.')
            return 0
        else:
            print(f'O valor é numérico e é {n}.')
            return 0


# Programa principal
leiaInt('Digite um número inteiro: ')
leiaFloat('Digite um número flutuante: ')