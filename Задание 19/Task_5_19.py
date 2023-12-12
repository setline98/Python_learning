import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    step=0.01
    x = np.arange(-3, 3, step)
    y = np.arange(-3, 3, step)
    X,Y = np.meshgrid(x,y)
    Z = X**2-Y**2+X
    plt.figure(1)
    plt.contourf(X, Y, Z)
    plt.savefig("Fig1.png")
    ax=Axes3D(plt.figure(2))
    ax.plot_surface(X, Y, Z)
    plt.savefig("Fig2.png")
    plt.show()

    return 0
if __name__ == '__main__':
    main()