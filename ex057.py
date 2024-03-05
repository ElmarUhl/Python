
sex = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while sex not in 'MF':
    sex = str(input('Opção inválida, digite o sexo [M/F] novamente: ')).strip().upper()[0]
print('O sexo escolhido foi {}'.format(sex))
