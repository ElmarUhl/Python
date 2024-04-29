import random

students = ['','','','']

i = 0
while (i < 4):
    students[i] = input('Type the name of a student: ')
    i += 1

print('The student chosen is {}'.format(students[random.randint(0,3)]))

print('The student chosen is {}.'.format(random.choice(students)))