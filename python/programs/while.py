n = 1
par = impar = 0
while n != 0:
    n = int(input('Type a value: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('You input {} even numbers and {} odd numbers'.format(par, impar))
