
number = int(input('Type a integer number: '))
print("""Type:
    (1) to convert to binary.
    (2) to convert to octal.
    (3) to convert to hexadecimal.""")

n = int(input('Choose a option: '))

if n == 1:
    print('{} converted to binary is {}'.format(number, bin(number)[2:]))
elif n == 2:
    print('{} converted to octal is {}'.format(number, oct(number)[2:]))
elif n == 3:
    print('{} converted to hexadecimal é {}'.format(number, hex(number)[2:]))
else:
    print('Invalid option')
