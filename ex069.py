continua = 'Y'

mem = 0
womem = 0
older = 0

while continua == 'Y':
    idade = int(input('Type the age: '))

    continua = ' '
    sex = ' '    
    while sex not in 'MF':
        sex = input('Type the gender [M/F]: ').strip().upper()[0]
    
    if sex == 'M':
        mem += 1
    else:
        if idade < 20:
            womem += 1
    
    if idade > 18:
        older += 1
    
    while continua not in 'YN':
        continua = input('Continue [y/n]: ').strip().upper()

print('Foram cadatrados {} homen, {} mulheres com menos 20 anos e {} pessoas com mais 18 anos'.format(mem, womem, older))

