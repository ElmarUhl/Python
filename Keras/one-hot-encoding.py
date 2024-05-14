import numpy as np

pessoas = ['Ana', 'Paula', 'Julia']

def normalize(nome):
    array = np.zeros(len(pessoas))
    for i, pessoa in enumerate(pessoas):
        if pessoa == nome:
            array[i] = 1.0
    return array

for pessoa in pessoas:
    print(f'{pessoa} - {normalize(pessoa)}')