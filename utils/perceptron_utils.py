import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng

def generate_random_data(n):
  return default_rng().random((1,n))

def plot_random_data():
  fig, ax = plt.subplots()
  ax.scatter(generate_random_data(10), generate_random_data(10), c='blue')
  ax.scatter(3*generate_random_data(10), 2*generate_random_data(10), c='red')
  plt.show()

# Assumes y in {-1, 1}
def training_loop(X, Y, rate, epochs):
  w = default_rng().random((1,2))
  b = default_rng().random()
  for _ in range(epochs):
    for i in range(len(X)):
      x = X[i]
      y = Y[i]
      w = w + rate*y*x
      b = b + rate*y
      print(w, b)
  return w, b

# TODO: this seems wrong
def generate_data():
  positive = default_rng().random((10, 2))
  skew = np.array([[3,0],[0,2]])
  positive = positive.dot(skew)
  negative = default_rng().random((10, 2))
  X = np.concatenate((positive, negative), axis=0)
  Y = np.concatenate((np.ones(10), -np.ones(10)))
  return X, Y

def plot_X(X):
  fig, ax = plt.subplots()
  positive = X[:10]
  negative = X[10:]
  for x in positive:
    ax.scatter(x[0], x[1], c='blue')
  for x in negative:
    ax.scatter(x[0], x[1], c='red')
  # plt.show()

# TODO: this seems wrong
def plot_line(w,b):
  w = w[0]
  x_min, x_max = 0, 5
  y_min = -(w[0]/w[1]) * x_min - b/w[1]
  y_max = -(w[0]/w[1]) * x_max - b/w[1]
  plt.plot([x_min, x_max], [y_min, y_max])