
distance = float(input('Type distance in km: '))

if distance > 200:
   print('The trip costs R$ {:.2f}'.format(distance*0.45)) 
else:
    print('The trip costs R$ {:.2f}'.format(distance*0.50))

    