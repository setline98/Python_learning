# task4.py
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def main():
    N = 1024
    t = np.arange(N)
    sig_periodic = np.sin(2*np.pi*8*t/N) + 0.5*np.sin(2*np.pi*16*t/N)
    sig_quasi = np.sin(2*np.pi*8*t/N) + np.sin(2*np.pi*15*t/N)

    def logistic(x, r): return r*x*(1-x)
    x = 0.2
    for _ in range(1000): x = logistic(x, 4.0)
    sig_chaos = np.empty(N)
    for i in range(N):
        x = logistic(x, 4.0); sig_chaos[i] = x

    for s in (sig_periodic, sig_quasi, sig_chaos):
        s -= s.mean()

    fft_per = np.abs(np.fft.fft(sig_periodic))[:N//2]
    fft_qua = np.abs(np.fft.fft(sig_quasi))[:N//2]
    fft_cha = np.abs(np.fft.fft(sig_chaos))[:N//2]
    freq = np.arange(N//2)

    plt.figure(figsize=(12,4))
    plt.subplot(1,3,1); plt.plot(freq, fft_per); plt.title('Периодический'); plt.grid(True)
    plt.subplot(1,3,2); plt.plot(freq, fft_qua); plt.title('Квазипериодический'); plt.grid(True)
    plt.subplot(1,3,3); plt.plot(freq, fft_cha); plt.title('Хаотический'); plt.grid(True)
    plt.tight_layout(); plt.show()

if __name__ == '__main__':
    main()
