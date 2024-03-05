number = int(input('Type a number: '))

unit = number % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousands = number // 1000 % 10

print('Unit: {}'.format(unit))
print('Ten: {}'.format(ten))
print('Hundred: {}'.format(hundred))
print('Thousands: {}'.format(thousands))
