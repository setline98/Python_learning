import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle as rick


def main():
    length = int(input("Введите кол-во учеников: "))
    f = open("Зачет.txt", "w")
    i = 0
    while i < length:
        f.write(inputData(i))
        i += 1

    return 0


def inputData(i):
    i = i + 1
    surname = str(input("Введите фамилию ученика " + str(i) + ":"))
    name = str(input("Введите имя ученика " + str(i) + ":"))
    sndname = str(input("Введите отчество ученика " + str(i) + ":"))
    mark = str(input("Введите оценку ученика " + str(i) + ":"))
    return str(str(i) + "\t" + surname + "\t" + name + "\t" + sndname + "\t" + mark + "\n")


if __name__ == '__main__':
    main()
