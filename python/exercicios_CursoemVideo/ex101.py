
def voto(ano):
    from datetime import date
    
    idade = date.today().year - ano
    if idade < 16:
        print('Não vota')
    elif idade >= 16 and idade < 18 or idade > 65:
        print('Voto OPCIONAL')
    else:
        print('Voto OBRIGATÓRIO')

    print(idade)

# Programa principal
n = int(input('Digite o ano de nascimento: '))
voto(n)
