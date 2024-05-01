import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

rng = default_rng()

n = 50
data_x = rng.integers(20, size=n)
data_y = rng.integers(12, size=n)

plt.scatter(x=data_x,y=data_y)
plt.show()
