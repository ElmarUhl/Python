expressao = input('Digite a expressão: ')
count = 0

for i in range(0, len(expressao)):
    if expressao[i] == '(':
        count += 1
    if expressao[i] == ')':
        count -= 1
    
print(expressao)
if count == 0:
    print('A expressão é válida')
else:
    print('A expressão é inválida')

