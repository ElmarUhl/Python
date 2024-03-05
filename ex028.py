from random import randint
from time import sleep

number = randint(0, 5)

number2 = int(input('Guess a number among 0 and 5: '))

print('-=-' * 20)
print('Processing...')
sleep(3)

if number == number2:
    print('Congratulations you got it right!')
else:
    print('You make a mistake! The number chosen is {}'.format(number))
