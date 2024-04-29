import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://www.pudim.com.br') # não funciona
    #site=urllib.request.urlopen('https://www.google.com/') #funciona
except urllib.request.URLError:
    print('Não foi possível acessar o site.')
else:
    print('O site está ativo e foi possível acessá-lo')