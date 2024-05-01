import numpy as np

a = np.array([1,2,3])
print('Original array')
print(a)
b = a[np.newaxis,:]
print('Array with new axis')
print(b)
print(f'This is number of array elements: {b.shape}')
print(f'This is number of array dimensions: {b.ndim}')
print()
c = a[:,np.newaxis]
print('Array with new axis')
print(c)
print(f'This is number of array elements: {c.shape}')
print(f'This is number of array dimensions: {c.ndim}')
