import numpy as np

x1 = [1,2,3]
x2 = [[1,2,3],[4,5,6],[7,8,9]]

a = np.empty((2,3))
b = np.eye(2,3,1)
c = np.identity(3)
d = np.ones((3,3))
e = np.zeros((3,3))
f = np.full((3,3),0.1)
g = np.array(x1)
h = np.asarray(x1)
i = np.asmatrix([1,2,3])
j = np.arange(3,10,1)
k = np.linspace(0, 10, 10)
l = np.diag(x2)
m = np.tri(3,3,0)
n = np.tril(x2)
o = np.triu(x2)

print(o)