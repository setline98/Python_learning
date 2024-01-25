import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle as rick


def main():
    f = open("2.txt", "w")
    x = np.arange(0, 2 * np.pi + np.pi / 24, np.pi / 24)
    for i in x:
        f.write(str(i) + "\t")
        f.write(str(m.sin(i)) + "\t")
        f.write(str(m.cos(i)) + "\n")
    return 0


if __name__ == '__main__':
    main()
