frase = 'Curso em video Python'
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print('Comprimento {}'.format(len(frase)))
print('Conta ocorrências {}'.format(frase.count('o')))
print('Conta ocorrencias {}'.format(frase.count('o',0,13)))
print('Procura {}'.format(frase.find('deo')))
print('Procura {}'.format(frase.find('Android')))
print('Procura {}'.format('Curso' in frase))
print('Maiusculas {}'.format(frase.upper()))
print('Minúsculas {}'.format(frase.lower()))
print('Capitalize {}'.format(frase.capitalize()))
print('Title {}'.format(frase.title()))
print('Remove espaco extras {}'.format(frase.strip()))
print('Remove espaços extras {}'.format(frase.rstrip()))
print('Remove espaços extras {}'.format(frase.lstrip()))
teste = frase.split()
print('Divisão de string {}'.format(teste))
print('Junção de strings {}'.format('-'.join(teste)))
print("""fjsdkdsksdjfdskjkkdkdskfsdkjsdkf
      sdkfjsdkdsjkdsjfsdkfjf
      ffkdsjfdskfjsdkfjsdfkfj""")
print('Replace {}'.format(frase.replace('Curso','Burro')))