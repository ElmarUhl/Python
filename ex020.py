import random

students = ['', '', '', '']

i = 0
while (i < 4):
    students[i] = input('The the student name: ')
    i += 1
    
random.shuffle(students)

print('The new sequence is {}'.format(students))
