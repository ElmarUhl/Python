from random import randint

alunos = ['','','','']

i = 0
while (i < 4):
    alunos[i] = input('Digite o nome de um dos alunos: ')
    i += 1

print('O aluno sorteado foi {}'.format(alunos[randint(0,3)]))