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

def slp_infer(x, w, b):
  return np.round(x*w+b)