import datetime

cadastro = {}

nome = input('Digite o nome: ')
ano = int(input('Digite o ano de nascimento: '))
ctps = int(input('Digite o número da carteira de trabalho: '))

cadastro['nome'] = nome
cadastro['idade'] = datetime.date.today().year - ano

if ctps != 0:
    cadastro['ano contração'] = int(input('Digite o ano de contratação: '))
    cadastro['salário'] = float(input(f'Digite o salário em R$: '))

aposenta = datetime.date.today().year - cadastro['ano contração']    
cadastro['aposenta'] = cadastro['idade'] + aposenta

print(cadastro)