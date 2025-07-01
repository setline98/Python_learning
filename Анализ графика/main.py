import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# Загрузка данных
with open("data-Titov.dat", "r") as file:
    data = np.array([float(line.strip()) for line in file])

# Построение исходного временного ряда
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title("Исходный временной ряд")
plt.xlabel("Время")
plt.ylabel("Значение")
plt.grid(True)
plt.tight_layout()
plt.show()

# Удаление линейного тренда
x = np.arange(len(data))
coeffs = np.polyfit(x, data, 1)
trend = np.polyval(coeffs, x)
minusTrend = data - trend

plt.figure(figsize=(10, 4))
plt.plot(minusTrend)
plt.title("Временной ряд без линейного тренда")
plt.xlabel("Время")
plt.ylabel("Значение")
plt.grid(True)
plt.tight_layout()
plt.show()

# Удаление периодической составляющей с помощью Фурье-преобразования
n = len(minusTrend)
frequencies = np.fft.fftfreq(n)
fft_values = np.fft.fft(minusTrend)

# Удалим низкочастотные компоненты
obrez = 0.0005
fft_values[np.abs(frequencies) < obrez] = 0

cleaned = np.fft.ifft(fft_values).real

plt.figure(figsize=(10, 4))
plt.plot(cleaned)
plt.title("Ряд без тренда и периодической составляющей")
plt.xlabel("Время")
plt.ylabel("Значение")
plt.grid(True)
plt.tight_layout()
plt.show()

# Построение графика сравнения спектров сигналов
fft_detrended = np.fft.fft(minusTrend)
fft_cleaned = np.fft.fft(cleaned)

# Спектры (модули) обеих версий сигнала
mag_detrended = np.abs(fft_detrended[:n // 2])
mag_cleaned = np.abs(fft_cleaned[:n // 2])
freqs = np.fft.fftfreq(n)[:n // 2]

plt.figure(figsize=(10, 4))
plt.plot(freqs, mag_detrended, label='После удаления тренда')
plt.plot(freqs, mag_cleaned, label='После удаления тренда и периодики')
plt.title("Сравнение спектров сигналов")
plt.xlabel("Частота")
plt.ylabel("Амплитуда спектра")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Расчёт статистик
sred = np.mean(cleaned)
sigma = np.std(cleaned)
ASSim = ((cleaned - sred) ** 3).mean() / sigma**3
eks = ((cleaned - sred) ** 4).mean() / sigma**4 - 3

print("Среднее:", sred)
print("Сигма (стандартное отклонение):", sigma)
print("Асимметрия:", ASSim)
print("Эксцесс:", eks)
print("Тренд:", trend)
