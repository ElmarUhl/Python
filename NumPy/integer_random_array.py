import numpy as np
from numpy.random import default_rng

rng = default_rng()

rand = rng.integers(10, size=(2,4))
print('This an array with integer random numbers')
print(rand)
