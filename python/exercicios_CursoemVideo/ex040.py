
n1 = float(input('Type the first grade: '))
n2 = float(input('Type the second grade: '))

media = (n1 + n2)/2.0

print('The media is {:.1f}'.format(media))

if media < 5.0:
    print('You disapproved')
elif media >= 5.0 and media <= 6.9:
    print('You are in recovery')
else:
    print('You approved')
    