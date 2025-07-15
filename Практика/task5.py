# task5.py

from __future__ import annotations
import os
import sys
from typing import List, Tuple
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import mne
from scipy import signal

# ---------------------------- НАСТРОЙКИ ------------------------------- #
FILE1: str = "Крыса бодровствует.edf"
FILE2: str = "Крыса спит.edf"
CHANNELS: List[str] = ["EEG EEG_1A-B", "EEG EEG_2A-B"]
WINDOW: float = 2.0     # сек
OVERLAP: float = 0.5    # сек
MAX_SEC: int | None = 120  # None = полностью
SCALES: np.ndarray = np.arange(1, 128)
FOURIER_FACTOR = 4.0

# --------------------------- ВСПОМОГАТЕЛЬНОЕ --------------------------- #

def load_channel(raw: mne.io.BaseRaw, ch_name: str) -> Tuple[np.ndarray, float]:
    """Возвращает сигнал канала и частоту дискретизации."""
    if ch_name not in raw.ch_names:
        raise ValueError(
            f"Канал '{ch_name}' не найден. Доступные каналы: {raw.ch_names}"
        )
    data = raw.copy().pick(ch_name).get_data()[0]
    sfreq = raw.info["sfreq"]
    return data, sfreq


# -------------------- СПЕКТРОГРАММА (ФУРЬЕ‑ОКНО) ------------------- #
def plot_spectrogram(
    signal_data: np.ndarray,
    fs: float,
    title: str,
    *,
    window: float,
    overlap: float,
) -> plt.Figure:

    nperseg = int(window * fs)
    noverlap = int(overlap * fs)
    freqs, times, sxx = signal.spectrogram(
        signal_data,
        fs,
        window="hann",
        nperseg=nperseg,
        noverlap=noverlap,
    )

    fig, ax = plt.subplots(figsize=(10, 4))
    im = ax.pcolormesh(times, freqs, 10 * np.log10(sxx + 1e-10), shading="auto")
    ax.set_title(f"{title} — Спектрограмма (оконное Фурье)")
    ax.set_xlabel("Время, с")
    ax.set_ylabel("Частота, Гц")
    ax.set_ylim(0, 50)  # верхний предел частоты
    fig.colorbar(im, ax=ax, label="Мощность, дБ")
    fig.tight_layout()
    return fig


# ----------------- ВЕЙВЛЕТ: «МЕКСИКАНСКАЯ ШЛЯПА» ------------------ #

def scales_to_freq(scales: np.ndarray, fs: float) -> np.ndarray:
    return fs / (FOURIER_FACTOR * scales)

def ricker_wavelet(points: int, scale: float) -> np.ndarray:
    """Генерирует дискретную волну Рикера."""
    t = np.linspace(-points / 2, points / 2, points)
    return (1 - (t / scale) ** 2) * np.exp(-(t**2) / (2 * scale**2))


def cwt_mexican_hat(signal_data: np.ndarray, scales: np.ndarray) -> np.ndarray:
    """Непрерывное вейвлет‑преобразование через NumPy."""
    coeffs = np.zeros((len(scales), len(signal_data)), dtype=float)
    for idx, scale in enumerate(scales):
        points = int(8 * scale) | 1  # нечётное число точек
        wavelet = ricker_wavelet(points, scale)
        wavelet /= np.sqrt(np.abs(scale))  # нормируем энергию
        coeffs[idx] = np.convolve(signal_data, wavelet, mode="same")
    return coeffs


def plot_wavelet(signal_data: np.ndarray, fs: float, title: str) -> plt.Figure:
    """Скалограмма (mexican‑hat) с pcolormesh и частотой по оси Y."""
    coeffs = cwt_mexican_hat(signal_data, SCALES)

    freqs = scales_to_freq(SCALES, fs)
    times = np.arange(len(signal_data)) / fs

    freqs = freqs[::-1]
    coeffs = coeffs[::-1]

    fig, ax = plt.subplots(figsize=(10, 4))
    pcm = ax.pcolormesh(times,
                        freqs,
                        np.abs(coeffs),
                        shading="auto",
                        cmap="viridis")

    ax.set_title(f"{title} — Вейвлет")
    ax.set_xlabel("Время, с")
    ax.set_ylabel("Частота, Гц")
    ax.set_ylim(0, 50)
    fig.colorbar(pcm, ax=ax, label="|W|, усл.ед.")
    fig.tight_layout()
    return fig

# ------------------------- ОБРАБОТКА ФАЙЛА -------------------------- #

def process_file(path: str, channels: List[str]) -> None:
    """Читает EDF и строит графики для заданных каналов."""
    if not os.path.isfile(path):
        sys.exit(f"Файл '{path}' не найден.")

    print(f"\nЧтение {path} …")
    raw = mne.io.read_raw_edf(path, preload=True, verbose="ERROR")

    for ch in channels:
        sig, fs = load_channel(raw, ch)
        if MAX_SEC is not None:
            sig = sig[: int(MAX_SEC * fs)]

        base = os.path.splitext(os.path.basename(path))[0]
        safe_ch = ch.replace(" ", "_")
        prefix = f"{base}_{safe_ch}"

        # --- спектрограмма
        fig_s = plot_spectrogram(sig, fs, prefix, window=WINDOW, overlap=OVERLAP)
        spec_png = f"{prefix}_spectrogram.png"
        fig_s.savefig(spec_png, dpi=150)
        print(f"  → сохранена спектрограмма: {spec_png}")

        # --- вейвлет‑скалограмма
        fig_w = plot_wavelet(sig, fs, prefix)
        wav_png = f"{prefix}_wavelet.png"
        fig_w.savefig(wav_png, dpi=150)
        print(f"  → сохранена карта вейвлета: {wav_png}")


# ------------------------------- MAIN ------------------------------- #

def main() -> None:
    """Точка входа программы."""
    for edf in (FILE1, FILE2):
        process_file(edf, CHANNELS)

    print("\nГотово. PNG‑файлы лежат рядом со скриптом.")


    if matplotlib.get_backend() != "Agg":
        plt.show()
    else:
        print("Backend 'Agg': графики не открываются автоматически.")


if __name__ == "__main__":
    main()