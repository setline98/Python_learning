import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle as rick
import os as os
import struct as struct


def main():
    # Создаем папку распределения, если ее нет
    if not os.path.exists("распределение"):
        os.mkdir("распределение")
        print("succeed")

    # Записываем три текстовых файла
    uniform_data = np.random.uniform(0, 1, 10000)
    normal_data = np.random.normal(0, 1, 10000)
    chi2_data = np.random.chisquare(5, 10000)

    np.savetxt("./распределение/uniform.txt", uniform_data, delimiter=',')
    np.savetxt("./распределение/normal.txt", normal_data, delimiter=',')
    np.savetxt("./распределение/chi2.txt", chi2_data, delimiter=',')

    # Переходим в папку распределения
    os.chdir("./распределение")

    # Находим все текстовые файлы
    files = [file for file in os.listdir() if file.endswith(".txt")]

    # Строим гистограммы распределений и сохраняем в файлы
    for file in files:
        data = np.loadtxt(file, delimiter=',')
        plt.hist(data, bins=200)
        plt.xlabel('Значения')
        plt.ylabel('Частота')
        plt.title(f"Гистограмма распределения ({file.split('.')[0]})")
        plt.savefig(file.split('.')[0] + ".png")
        plt.clf()  # Очищаем график для следующей итерации
    return 0


if __name__ == '__main__':
    main()
