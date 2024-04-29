lista = []

while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))

    aluno = []
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    lista.append(aluno[:])
    aluno.clear()
    
    option = input('Continua? [S/N]: ').strip().upper()[0]
    if option == 'N':
        break

for i in lista:
    print(f'{i[0]:.<20} média = {(i[1] + i[2])/2}')
    
while True:
    option = input('Deseja mostrar nota de algum aluno? [nome/N]: ').strip().upper()
    if option == 'N':
        break
    else:
        for i in lista:
            if i[0].upper() == option:
                print(f'{i[0]:.<20} média = {(i[1] + i[2])/2}')
