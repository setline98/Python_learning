import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle as rick


def main():
    name = int(input("Введите номер: "))
    fw = open(str("EGG_" + str(name) + ".txt"), "w")
    fr = open("EEG.txt", "r")
    
    for line in fr:
        mylist = line.split()
        fw.write(mylist[name - 1] + "\n")
    print("Готово")

    return 0


if __name__ == '__main__':
    main()
