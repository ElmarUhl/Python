pessoas = [['Pedro',25],['Maria',19],['João', 32]]
print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][0])
print(pessoas[1])

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19],['Ana',33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')

galerar = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)


