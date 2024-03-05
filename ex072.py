numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

number = -1
while number < 0 or number > 20:
    number = int(input('Digite um número entre 0 e 20: '))

print(f'O número digitado foi {numbers[number]}')
