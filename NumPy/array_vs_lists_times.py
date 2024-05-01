import numpy as np
from numpy.random import default_rng
from time import process_time

rng = default_rng()

# List
print('-'*50)
lista_a = list(rng.integers(10, 100, 10000000))
lista_b = list(rng.integers(10, 100, 10000000))
print('Generated two lists of 10,000,000 integer numbers between 10 and 100')
print('Two lists will be multiplicated and it will get the task processing time')
c = []
t1 = process_time()
for i in range(len(lista_a)):
    c.append(lista_a[i]*lista_b[i])
t2 = process_time()
t_list = t2 - t1
print(f'Task processing time: {t_list}s')
print()
# Array
a = rng.integers(10,100,10000000)
b = rng.integers(10,100,10000000)
print('Generated two arrays of 10,000,000 integer numbers between 10 and 100')
print('Two arrays will be multiplicated and it will get the task processing time')
t1 = process_time()
c = a*b
t2 = process_time()
t_array = t2 - t1
print(f'Task processing time: {t_array}s')
print('-'*50)
print(f'The ratio between list and array is approximately {round(t_list/t_array,2)}')
print('-'*50)
