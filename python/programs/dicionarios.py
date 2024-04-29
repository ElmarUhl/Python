dados = dict()
dados['nome'] = 'João'
dados['idade'] = 40
dados['sexo'] = 'M'
del dados['sexo']

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
    
for i in brasil:
    for k, v in i.items():
        print(k, v)
        
for e in brasil:
    for v in e.values():
        print(v)
        
