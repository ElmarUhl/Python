import numpy as np
from keras.models import Sequential
from keras.layers import Dense

"""
Dormiu  Estudou Nota
8       3       7
10      4       8
10      5       9.5
5       7       4.5
5       10      5
10      6       10
"""

x = np.array([[8.0,3.0],[10.0,4.0],[10.0,5.0],[5.0,7.0],[5.0,10.0],[10.0,6.0]])
x = x/10
y = np.array([[7.0],[8.0],[9.5],[4.5],[5.0],[10.0]])
y = y/10

#x = np.array([[0.1], [0.11], [0.12], [0.15], [0.2], [0.21], [0.22], [0.3]])
#y = 2*x

model = Sequential()

model.add(Dense(3,input_dim=2))
model.add(Dense(1))

model.compile(optimizer='sgd', loss='mse', metrics=['acc'])
model.fit(x,y, epochs= 3000)

while True:
    dormiu = input('Digite quantas horas vc dormiu: ')
    estudou = input('Digite quantas horas você estudou: ')
    
    lista = [float(dormiu)/10, float(estudou)/10]
    t = np.asmatrix(lista)
    result = model.predict(t)

    print(f'Dormiu {float(dormiu)*10} e estudou {float(estudou)*10} - nota: {result[0][0]*10}')
