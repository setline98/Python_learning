# task3.py
# Статистические характеристики логистического отображения
#Добавить графики АКФ

import numpy as np


def logistic(x, r):
    return r * x * (1 - x)


def generate_series(r, N=1000, discard=100, x0=0.1):
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


if __name__ == '__main__':
    main()
