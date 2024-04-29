from datetime import date

anoNascimento = int(input('Digite o ano de nascimento:'))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

if idade < 9:
    print('Idade {} anos. Você está na categoria MIRIM'.format(idade))
elif idade >= 9 and idade < 14:
    print('Idade {} anos. Você está na categoria INFANTIL'.format(idade))
elif idade >= 14 and idade < 19:
    print('Idade {} anos. Você está na categoria JUNIOR'.format(idade))
elif idade >= 19 and idade < 20:
    print('Idade {} anos. Você está na categoria SÊNIOR'.format(idade))
else:
    print('Idade {} anos. Você está na categoria MASTER'.format(idade))
