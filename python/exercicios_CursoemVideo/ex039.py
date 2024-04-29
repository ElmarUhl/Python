from datetime import date

yBirth = int(input('Type the year of birth: '))

yNow = date.today()
y = yNow.year - yBirth

if y < 17:
    print('You must enlistment in {} year.'.format(17 - y))
elif y == 17:
    print('You are in enlistment')
else:
    print('You past {} year from enlistment.'.format(y - 17))
