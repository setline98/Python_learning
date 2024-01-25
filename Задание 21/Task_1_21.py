import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle as rick
import os as os
import struct as struct


def main():
    NumberChannel = int(input("Введите номер: ")) - 1
    length = 100  # количество измерений
    Rat = 'Rat.wdq'
    fr = open(Rat, 'rb')
    buffer = fr.read(length * 2 * 4)
    mylist = struct.unpack(length * 4 * 'h', buffer)
    channel = mylist[NumberChannel::4]
    file = os.path.join(os.getcwd(), Rat)  # указываем полный путь к файлу
    fw = open(os.path.splitext(file)[0] + str(NumberChannel) + '.txt', 'w')
    for i in range(len(channel)):
        fw.write(str(channel[i]) + '\n')
    fw.close()

    return 0


if __name__ == '__main__':
    main()
