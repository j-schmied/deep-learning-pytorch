import matplotlib.pyplot as plt
import numpy as np


def z_function(x, y):
    return np.sin(5*x) * np.cos(5*y) / 5


def calculate_gradient(x, y):
    return np.cos(5*x) * np.cos(5*y), -np.sin(5*x) * np.sin(5*y)


def main():
    x = np.arange(-1, 1, 0.05)
    y = np.arange(-1, 1, 0.05)
    
    X, Y = np.meshgrid(x, y)
    Z = z_function(X, Y)
    
    current_position1 = (0.7, 0.4, z_function(0.7, 0.4))
    current_position2 = (0.3, 0.8, z_function(0.3, 0.8))
    current_position3 = (-0.5, 0.5, z_function(-0.5, 0.5))


    learning_rate = 0.01
    
    ax = plt.subplot(projection="3d", computed_zorder=False)
    
    for _ in range(1000):
        X_derivative, Y_derivative = calculate_gradient(current_position1[0], current_position1[1])
        X_new, Y_new = current_position1[0] - learning_rate * X_derivative, current_position1[1] - learning_rate * Y_derivative
        current_position1 = (X_new, Y_new, z_function(X_new, Y_new))
        
        X_derivative, Y_derivative = calculate_gradient(current_position2[0], current_position2[1])
        X_new, Y_new = current_position2[0] - learning_rate * X_derivative, current_position2[1] - learning_rate * Y_derivative
        current_position2 = (X_new, Y_new, z_function(X_new, Y_new))
        
        X_derivative, Y_derivative = calculate_gradient(current_position3[0], current_position3[1])
        X_new, Y_new = current_position3[0] - learning_rate * X_derivative, current_position3[1] - learning_rate * Y_derivative
        current_position3 = (X_new, Y_new, z_function(X_new, Y_new))
    
        ax.plot_surface(X, Y, Z, cmap="viridis", zorder=0)
        ax.scatter(current_position1[0], current_position1[1], current_position1[2], color="magenta", zorder=1)
        ax.scatter(current_position2[0], current_position2[1], current_position2[2], color="green", zorder=1)
        ax.scatter(current_position3[0], current_position3[1], current_position3[2], color="cyan", zorder=1)
        plt.pause(0.001)
        ax.clear()


if __name__ == "__main__":
    main()
