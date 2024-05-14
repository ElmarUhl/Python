# Normaliza os valores
pesos = [56.4, 89.63, 123.4, 78.45]
maior = max(pesos)

for peso in pesos:
    valor = peso/maior
    print(f'{peso} "=>" {valor}')
