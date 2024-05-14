import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Dados para aprendizado
x = np.array([[0.1], [0.11], [0.12], [0.15], [0.2], [0.21], [0.22], [0.3]])
y = 2*x
#y = np.array([[0.2], [0.30], [0.4],[0.6]])

modelo = Sequential() # modelo

# Cria o modelo do tipo  perceptron com 
# 1 dimensão na entrada e 1 saída
modelo.add(Dense(1, input_dim=1)) # add a camada

# optimizer - como os pesos são atualizados (sgd = stochastic gradient descent)
# loss - como os erros são calculados (mse = mean square error)
# metrics - acurácia do modelo (acc = accuracy)
modelo.compile(optimizer='sgd', loss='mse', metrics=['acc'])
modelo.fit(x, y, epochs=2000) # Treina a rede neural com os dados x e y

# Testa os valores
while True:
    t = float(input('Digite um número: '))
    t = np.asmatrix(t) # necessário converter para matrix no keras
    result = modelo.predict(t)
    print(f'Valor de entrada: {t} e previsto pela rede neural: {result[0]}')
