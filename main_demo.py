import matplotlib.pyplot as plt
import utils.perceptron_utils as utils

def main():
  # utils.plot_random_data()
  X, Y = utils.generate_data()
  utils.plot_X(X)
  w, b = utils.training_loop(X,Y,0.01,10)
  utils.plot_line(w,-10)
  plt.show()

main()