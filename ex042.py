lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado:'))
lado3 = float(input('Digite o terceiro lado:'))

lados = [lado1, lado2, lado3]

lados.sort()

condicao1 = False
condicao2 = False
if (lado1 + lado2) > lado3:
    condicao1 = True
if ((lado3 - lado2) < lado1):
    condicao2 = True
    
if condicao2 and condicao1:
    print('É triângulo')
    if lados[0] == lados[1] and lados[0] == lados[2] and lados[1] == lados[2]:
        print('O triângulo é equilátero')
    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Não é triângulo')
