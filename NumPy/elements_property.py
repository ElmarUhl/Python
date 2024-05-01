import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print('Prints even elements of array')
print(a[a%2 == 0])
