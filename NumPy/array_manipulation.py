import numpy as np

a = [[1,2,3],[3, 4, 5]]
a = np.array(a)

print(a)

print(np.shape(a))
print(np.reshape(a,(3,2)))
print(np.ravel(a))
print(a.flat[4])
a.itemset(3, 4)
print(a)
print(a.max())
print(a.mean())
print(a.min())
print(a.nonzero())
print(a.prod())
print(np.repeat(3,4))
print(np.append([1,2,3],[1,2,3]))
print(np.resize(a,(3,3)))
b = np.array([1,0,2,3,4,0])
print(np.trim_zeros(b))
print(np.unique(a))
print(np.flip(a))
print(np.roll(a,1))
