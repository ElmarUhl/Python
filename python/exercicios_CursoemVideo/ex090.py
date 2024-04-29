nome = input('Digite o nome do aluno: ')
media = float(input('Digite a média do aluno: '))

cadastro = dict()
cadastro['nome'] = nome
cadastro['média'] = media

if media >= 7:
    cadastro['situação'] = 'aprovado'
elif 5 < media and media < 7:
    cadastro['situação'] = 'recuperação'
else:
    cadastro['situação'] = 'reprovado'
    
print(f'O aluno {cadastro["nome"]} tem média {cadastro["média"]} e está {cadastro["situação"]}.')