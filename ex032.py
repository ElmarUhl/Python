
y = int(input('Type the year: '))

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('It is leap year')
else:
    print('It is not leap year')
    