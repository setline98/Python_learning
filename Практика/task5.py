# task5.py
# Упрощённая классификация ЭЭГ-сигналов

import numpy as np


def band_power(signal, f_low, f_high, fs):
    freqs = np.fft.rfftfreq(len(signal), 1.0 / fs)
    psd = np.abs(np.fft.rfft(signal * np.hanning(len(signal)))) ** 2
    mask = (freqs >= f_low) & (freqs <= f_high)
    return psd[mask].sum()


def main():
    fs = 100
    T = 5.0
    N = int(fs * T)
    t = np.linspace(0, T, N, endpoint=False)

    # Сигнал 1: нормальный ЭЭГ с альфа-ритмом 10 Гц
    sig1 = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
    sig1 += 0.5 * np.random.randn(N)

    # Сигнал 2: патологический - медленный ритм + спайк
    sig2 = 1.5 * np.sin(2 * np.pi * 3 * t) + 0.5 * np.random.randn(N)
    spike_idx = int(2.0 * fs)
    if spike_idx + 5 < N:
        sig2[spike_idx:spike_idx + 5] += 5.0

    signals = {'Сигнал 1': sig1, 'Сигнал 2': sig2}
    results = {}

    for name, sig in signals.items():
        mu = sig.mean()
        sigma = sig.std()
        kurt = ((sig - mu) ** 4).mean() / sigma ** 4 - 3
        delta = band_power(sig, 0.5, 4.0, fs)
        alpha = band_power(sig, 8.0, 12.0, fs)
        results[name] = dict(mu=mu, sigma=sigma, kurt=kurt, delta=delta, alpha=alpha)

    for name, res in results.items():
        print(f'{name}:')
        print(f'  μ = {res["mu"]:.3f}, σ = {res["sigma"]:.3f}, kurt = {res["kurt"]:.3f}')
        print(f'  Δ-power = {res["delta"]:.2f}, α-power = {res["alpha"]:.2f}')

    # простейший классификатор
    class1 = 1 if results['Сигнал 1']['alpha'] > results['Сигнал 1']['delta'] else 2
    class2 = 1 if results['Сигнал 2']['alpha'] > results['Сигнал 2']['delta'] else 2
    print(f'\nКлассификация: Сигнал 1 → класс {class1}, Сигнал 2 → класс {class2}')


if __name__ == '__main__':
    main()
