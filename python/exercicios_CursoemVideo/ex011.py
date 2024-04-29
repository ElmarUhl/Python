
width = float(input('Type width of wall in meters: '))
height = float(input('Type height of wall in meters: '))

area = height * width
inkLiters = area/2

print('The area of wall is {} and it needs {} liters of ink to paint it.'.format(area, inkLiters))
