import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle as rick


def main():
    f = open("1.txt", "w")
    n = np.arange(0, 101)
    for i in n:
        f.write(str(i) + "\t")
        f.write(str(i * i) + "\t")
        f.write(str(i * i * i) + "\n")
    return 0


if __name__ == '__main__':
    main()
