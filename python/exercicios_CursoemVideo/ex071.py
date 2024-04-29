value = int(input('Digite o valor a ser sacado: '))

n50 = 0
n20 = 0
n10 = 0
n1 = 0

if value >= 50:
    n50 = value // 50

temp = value - n50*50

if temp >= 20:
    n20 = temp // 20
    
temp = temp - n20*20
if temp >= 10:
    n10 = temp // 10

temp = temp - n10*10
if temp >= 1:
    n1 = temp 
    
print("""Você receberá:
      {} notas de R$ 50,00
      {} notas de R$ 20,00
      {} notas de R$ 10,00
      {} notas de R$ 1,00""".format(n50, n20, n10, n1))
