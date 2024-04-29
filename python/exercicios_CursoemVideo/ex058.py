from random import randint

number = randint(0, 10)
guess = int(input('Guess a number: '))
n = 1

while number != guess:
    print('You is wrong, try again!')
    guess = int(input('Guess a number: '))
    n += 1

print('Congratulations, you got it right in {} attempts!'.format(n))