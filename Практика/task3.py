# task3.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
def logistic(x, r):
    return r * x * (1 - x)

def generate_series(r, N=200, discard=100, x0=0.1):
    x = x0
    for _ in range(discard):
        x = logistic(x, r)
    series = np.empty(N)
    for i in range(N):
        x = logistic(x, r)
        series[i] = x
    return series

def autocorr(x, lag):
    if lag >= len(x):
        return 0.0
    return np.corrcoef(x[:-lag], x[lag:])[0, 1]

def main():
    for r in [3.2, 4.0]:
        data = generate_series(r)
        mu = data.mean()
        sigma = data.std()
        skew = ((data - mu) ** 3).mean() / sigma ** 3
        kurt = ((data - mu) ** 4).mean() / sigma ** 4 - 3
        ac1 = autocorr(data, 1)
        ac2 = autocorr(data, 2)
        regime = 'хаос' if r >= 3.57 else 'период'
        print(f'r = {r} ({regime}):')
        print(f'  Среднее = {mu:.4f}, σ = {sigma:.4f}')
        print(f'  Асимметрия = {skew:.4f}, Эксцесс = {kurt:.4f}')
        print(f'  АКФ лаг 1 = {ac1:.4f}, лаг 2 = {ac2:.4f}\n')

        # Графики сигнала и его автокорреляционной функции
        N = len(data)
        max_lag = N // 2
        acf_vals = []
        for lag in range(max_lag):
            if lag == 0:
                acf_vals.append(1.0)
            else:
                acf_vals.append(np.corrcoef(data[:-lag], data[lag:])[0, 1])
        acf_vals = np.array(acf_vals)
        t_vals = np.arange(max_lag)
        plt.figure(figsize=(6,5))
        plt.subplot(2, 1, 1)
        plt.plot(t_vals, data[:max_lag])
        plt.title(f'Сигнал (r = {r})')
        plt.xlabel('Время')
        plt.ylabel('x(t)')
        plt.grid(True)
        plt.subplot(2, 1, 2)
        plt.plot(t_vals, acf_vals)
        plt.title('Коррелограмма')
        plt.xlabel('Время')
        plt.ylabel('АКФ')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    main()
