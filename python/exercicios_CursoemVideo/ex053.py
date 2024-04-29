# Testa de uma frase é palindromo

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
frase = junto

l = len(frase)

palindromo = True
for c in range(0, l//2):
    print('{} {}'.format(frase[c], frase[l - c - 1]))
    if frase[c] != frase[l - c - 1]:
        palindromo = False
        
if palindromo:
    print('é palíndromo')
else:
    print('Não é palíndromo')
 
    
inverso = junto[::-1]
print(junto)
print(inverso)

if junto == inverso:
    print('é palíndromo')
