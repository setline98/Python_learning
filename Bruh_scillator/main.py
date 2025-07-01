import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Или "QtAgg", если "TkAgg" не работает

import matplotlib.pyplot as plt
from scipy.stats import norm

def main():
    with open("data-3485-1.00-1.985--0.02-10000-Titov.dat", "r") as file:
        data = np.array([float(line.strip()) for line in file])


    mean_value = np.mean(data)
    sigma_value = np.std(data)


    x_values = np.linspace(mean_value - 3 * sigma_value, mean_value + 3 * sigma_value, 1000)
    theoretical_gaussian = norm.pdf(x_values, mean_value, sigma_value)


    step = sigma_value / 10
    exp_x_values = np.arange(mean_value - 3 * sigma_value, mean_value + 3 * sigma_value, step)
    hist_values, bin_edges = np.histogram(data, bins=exp_x_values, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    interpolated_theoretical = norm.pdf(bin_centers, mean_value, sigma_value)
    residuals = np.sum((hist_values - interpolated_theoretical) ** 2)


    sigma_intervals = [1, 2, 3, 4, 5]
    percentages = {
        f"{s} sigma": np.sum((data >= mean_value - s * sigma_value) & (data <= mean_value + s * sigma_value)) / len(
            data) * 100
        for s in sigma_intervals
    }
    # Вывод результатов
    print(f"Значение (μ): {mean_value:.5f}")
    print(f"Стандартное отклонение (σ): {sigma_value:.5f}")
    print(f"Невязка (сумма квадратов разностей): {residuals:.5f}")
    print("Процент значений в пределах интервалов:")
    for k, v in percentages.items():
        print(f"  {k}: {v:.2f}%")

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, theoretical_gaussian, label="Теоретическое распределение", color="blue")
    plt.plot(bin_centers, hist_values, label="Экспериментальное распределение", color="red", linestyle="dashed")
    plt.xlabel("Значения")
    plt.ylabel("Плотность вероятностей")
    plt.title("Сравнение теоретического и экспериментального распределения")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()