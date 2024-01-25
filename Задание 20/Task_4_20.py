import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle as rick


def main():
    name = str(input("Введите фамилию для поиска: "))
    f = open("Зачет.txt", "r")
    for line in f:
        mylist = line.split()
        if mylist[1] == name:
            print(str(mylist[1]), str(mylist[4]))
            return 0
    print("Такой не найден")

    return 0


if __name__ == '__main__':
    main()
