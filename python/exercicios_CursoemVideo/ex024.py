city = input('Type the name of city: ')

begin = city.split()

if begin[0].upper() == 'SANTO':
    print('Yes, the city begins with Santo')
else:
    print('No, the city does not begin with Santo')
