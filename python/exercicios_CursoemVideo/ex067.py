n = 0
while True:
    n = int(input('Type a number to see the multiplication table: '))
    if n < 0:
        break
    
    for c in range(0, 10):
        print(f'{n} x {c} = {n*c}')
