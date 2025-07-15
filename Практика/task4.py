# task4.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

def logistic(x):
    return 4 * x * (1 - x)

def main():
    N = 1024
    t = np.arange(N)

    sig_p = np.sin(2 * np.pi * 8 * t / N) + 0.5 * np.sin(2 * np.pi * 16 * t / N)
    sig_q = np.sin(2 * np.pi * 8 * t / N) + np.sin(2 * np.pi * 15 * t / N)

    x = 0.2
    for _ in range(1000):
        x = logistic(x)
    sig_c = np.array([logistic(x := logistic(x)) for _ in range(N)])

    signals = [sig_p, sig_q, sig_c]
    labels = ['Периодический', 'Квазипериодический', 'Хаотический']

    freq = np.fft.rfftfreq(N, 1)
    spectra = [np.abs(np.fft.rfft(s - s.mean())) for s in signals]

    fig, axes = plt.subplots(2, 3, figsize=(12, 6))
    for i, (s, l) in enumerate(zip(signals, labels)):
        axes[0, i].plot(t, s)
        axes[0, i].set(title=l, xlabel='Время', ylabel='Амплитуда')
        axes[0, i].grid()

        axes[1, i].plot(freq, spectra[i])
        axes[1, i].set(title=f'Спектр {l}', xlabel='Частота', ylabel='Амплитуда')
        axes[1, i].grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

