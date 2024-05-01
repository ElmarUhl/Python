import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
print('This the original arrays')
print(f'{a}\t{b}')
print()
c = np.concatenate((a,b))
print('This is concatenated array')
print(c)
