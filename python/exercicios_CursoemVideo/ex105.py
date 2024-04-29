def notas(*notas, sit=True):
    """
    -> notas(n1,n2,..., sit).
    ;n1, n2,... params: relação de notas
    ;sit param: flag para incluir situação no dicionário
    ;return: retorna um dicionário com o número de notas lidas, a maior e a menor nota, a média das notas e sit=True inclui a situação da turma que é boa se a média >= 7, regular se 5 <= média < 7 e ruim se media < 5
    """
    d = dict()
    n = len(notas)
    d['n° notas'] = n
    temp = []
    soma = 0
    for i in notas:
        temp.append(i)
        soma += i
    d['maior'] = max(temp)
    d['menor'] = min(temp)
    media = soma/n
    d['media'] = round(media, 1)
    if sit:
        if media >= 7:
            d['situação'] = 'boa'
        elif media < 7 and media >= 5:
            d['situação'] = 'regular'
        else:
            d['situação'] = 'ruim'
    return d

d = notas(3, 4, 5, 5, 9, 3, sit=False)
print(d)