
speed = int(input('Type the speed: '))

if speed > 80:
    print('You exceed limit of 80 km/h')
    tax = (speed - 80)*7
    print('You was penalty and its value is R$ {:.2f}'.format(tax))
else:
    print('You are in limit of 80 km/h')
