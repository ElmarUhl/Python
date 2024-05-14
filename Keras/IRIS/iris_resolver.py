import numpy as np
import pandas as dp

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

from sklearn.preprocessing import LabelEncoder

df = dp.read_csv('iris.csv')

dataset = df.values

x = dataset[:,0:4].astype('float')
y = dataset[:,4]

encoder = LabelEncoder()
encoded = encoder.fit_transform(Y)

print(encoder)
