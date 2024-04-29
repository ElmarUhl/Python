
valueHome = float(input('Type the value of house: '))
valueSalary = float(input('Type the value of salary: '))
y = int(input('Type the years to pay off: '))

prest = float(valueHome / (12*y))

if prest > 0.30 * valueSalary:
    print('Negative loan')
else:
    print('Your quota is R$ {:.2f}'.format(prest))