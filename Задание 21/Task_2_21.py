import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle as rick
import os as os
import struct as struct


def main():
    with open('rat_01_02ml.wdq', 'rb') as file:
        file.seek(5296)
        data = file.read()

    channel_data = struct.unpack(len(data) // 2 * 'h', data)
    time = np.linspace(0, (len(channel_data) // 4) * 0.00195, len(channel_data) // 4)

    # Создаем 4 графика для каждого канала
    fig, axs = plt.subplots(4, 1, figsize=(10, 8))
    # Построение графиков
    # Канал 1
    axs[0].plot(time, channel_data[::4])
    axs[0].set_title('Channel 1')
    # Канал 2
    axs[1].plot(time, channel_data[1::4])
    axs[1].set_title('Channel 2')
    # Канал 3
    axs[2].plot(time, channel_data[2::4])
    axs[2].set_title('Channel 3')
    # Канал 4
    axs[3].plot(time, channel_data[3::4])
    axs[3].set_title('Channel 4')
    # Добавление подписей к осям и отображение графиков
    plt.xlabel('Time')
    plt.show()
    return 0


if __name__ == '__main__':
    main()
