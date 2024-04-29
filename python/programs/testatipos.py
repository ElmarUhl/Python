# Testa tipos de entrada

data = input("Digite algo: ")

print('Tipo primitivo é ', type(data))
print('Vc digitou: {}'.format(data))
print('É alfanumérico: ', data.isalnum())
print('É alfabético: ', data.isalpha())
print('É ascii: ', data.isascii())
print('É decimal: ', data.isdecimal())
print('É digito: ', data.isdigit())
print('É identificador: ', data.isidentifier())
print('É minúsculo: ', data.islower())
print('Pode ser impresso: ', data.isprintable())
print('É espaço: ', data.isspace())
print('É título: ', data.istitle())
print('É maiúsculo: ', data.isupper())
print('É número: ', data.isnumeric())
