import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a)
print(f'Dimensions of array: {a.shape}')
print(f'Size of array: {a.size}')
print(f'Number of array dimensions: {a.ndim}') # número de dimensões do array

b = np.array([1,2,3])
print(b)
print(f'Number of array dimensions: {b.ndim}')
