peso = int(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))

imc = float(peso/altura**2)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você esta com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')
