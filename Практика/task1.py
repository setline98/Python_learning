# task1.py
# Бифуркационная диаграмма отображения Эно и оценка постоянной Фейгенбаума
# Сравнить постоянную фейгенбаума с эталонным значением

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def main():
    # Параметры отображения Эно
    b = 0.3
    a_values = np.arange(1.0, 1.4, 0.001)
    # Начальные условия
    x, y = 0.0, 0.0

    a_list, x_list = [], []
    prev_x, prev_y = x, y
    first = True

    # Итерация по параметру a
    for a in a_values:
        skip = 500 if first else 100   # пропуски для выхода на аттрактор
        first = False
        collect = 100                  # точек на аттракторе

        # старт с предыдущего состояния для ускорения
        x, y = prev_x, prev_y

        # пропустить транзиент
        for _ in range(skip):
            x, y = 1 - a * x * x + y, b * x

        # собрать точки
        for _ in range(collect):
            x, y = 1 - a * x * x + y, b * x
            a_list.append(a)
            x_list.append(x)

        prev_x, prev_y = x, y

    # Построение бифуркационной диаграммы
    plt.figure(figsize=(8, 5))
    plt.scatter(a_list, x_list, s=0.5, color='black')
    plt.title('Бифуркационная диаграмма Эно (b = 0.3)')
    plt.xlabel('a')
    plt.ylabel('x на аттракторе')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # --- Оценка постоянной Фейгенбаума ---
    def find_period(a_val):
        x, y = 0.0, 0.0
        for _ in range(1000):
            x, y = 1 - a_val * x * x + y, b * x
        seq = []
        for _ in range(32):
            x, y = 1 - a_val * x * x + y, b * x
            seq.append(x)
        for T in [1, 2, 4, 8, 16]:
            if all(abs(seq[i] - seq[i + T]) < 1e-6 for i in range(T)):
                return T
        return 0  # хаос / большой период

    def find_transition(low, high, target_period):
        # бинарный поиск значения a, при котором период становится target_period
        for _ in range(30):
            mid = 0.5 * (low + high)
            p = find_period(mid)
            if p >= target_period or p == 0:
                high = mid
            else:
                low = mid
        return 0.5 * (low + high)

    a1 = find_transition(0.1, 0.5, 2)
    a2 = find_transition(a1, 1.0, 4)
    a3 = find_transition(a2, 1.1, 8)

    if (a3 - a2) != 0:
        delta = (a2 - a1) / (a3 - a2)
    else:
        delta = None

    print('\nПриблизительные критические значения параметра a:')
    print(f' a1 (1->2): {a1:.6f}')
    print(f' a2 (2->4): {a2:.6f}')
    print(f' a3 (4->8): {a3:.6f}')
    if delta is not None:
        print(f'Оценка постоянной Фейгенбаума δ ≈ {delta:.3f}')
    else:
        print('Не удалось вычислить δ (деление на ноль)')


if __name__ == '__main__':
    main()
