
r1 = float(input('Type the length of first segment: '))
r2 = float(input('Type the length of second segment: '))
r3 = float(input('Type the length of third segment: '))

list = [r1, r2, r3]
list.sort()

condition11 = False
condition2 = False

if list[2] < (list[0] + list[1]):
    condition1 = True
else:
    condition1 = False
    
if (list[2] - list[1]) < list[0]:
    condition2 = True
else:
    condition2 = False

if condition1 and condition2:
    print('The segments can forming a triangle')
else:
    print('The segments can not forming a triangle')
