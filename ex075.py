lista = ('boneco', 'comedor', 'malafaia')

for words in lista:
    print(f'Na palavra {words.upper()} temos ', end='')
    for letras in words:
        if letras in 'aeiou':
            print(f'{letras} ', end='')
    print('')
