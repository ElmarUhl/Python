largura = float(input('Digite a lagura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = altura * largura

litros_tinta = area/2

print('A área da parede é {} e são necessários {} litros de tinta para pintá-la.'.format(area,litros_tinta))
