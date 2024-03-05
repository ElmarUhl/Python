class Chachorros:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('au au')
    def correr(self):
        print(f'{self.nome} está correndo')

cachorro_1 = Chachorros('Tob', 'marrom', 5, 'grande')

print(cachorro_1.nome)
print(cachorro_1.idade)
cachorro_1.idade = 8
print(cachorro_1.idade)
cachorro_1.latir()
cachorro_1.correr()

cachorro_2 = Chachorros('Max', 'preto', 2, 'pequeno')
cachorro_2.correr()
