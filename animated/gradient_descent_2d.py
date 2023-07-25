import matplotlib.pyplot as plt
import numpy as np


def y_function(x):
    return np.sin(x)


def y_derivative(x):
    return np.cos(x)


def main():
    x = np.arange(-5, 5, 0.1)
    y = y_function(x)

    current_position = (1.5, y_function(1.5))
    learning_rate = 0.01

    for _ in range(1000):
        new_x = current_position[0] - learning_rate * y_derivative(current_position[0])
        new_y = y_function(new_x)
        current_position = (new_x, new_y)

        plt.plot(x, y)
        plt.scatter(current_position[0], current_position[1], color='r')
        plt.pause(0.001)
        plt.clf()
        

if __name__ == "__main__":
    main()
