from datetime import date

maiores = 0
menores = 0

for c in range(0, 7):
    n = int(input('Digite o ano de nascimento: '))
    dataAtual = date.today().year
    idade = dataAtual - n
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
        
print('São maiores de idade {} pessoas e menores de idade {} pessoas'.format(maiores, menores))

