def titulo():
    print('\033[1;30;42m')
    print('~'*30)
    print('{:^30}'.format('Sistema de Ajuda PyHelp'))
    print('~'*30, end='')
    print('\033[m')

    
def ajuda(txt):
    print('\033[7m', end='')
    help(i)
    print('\033[m')
    

while True:
    titulo()
    i = input('Função ou biblioteca > ')
    if i == 'FIM':
        break
    ajuda(i)