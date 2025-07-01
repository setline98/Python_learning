# task2.py
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def main():
    sigma, r, b = 10.0, 28.0, 8.0/3.0

    def lorenz(t, state):
        x, y, z = state
        return np.array([sigma*(y - x), x*(r - z) - y, x*y - b*z], dtype=float)

    def rk4_step(f, t, y, h):
        k1 = f(t, y)
        k2 = f(t + 0.5 * h, y + 0.5 * h * k1)
        k3 = f(t + 0.5 * h, y + 0.5 * h * k2)
        k4 = f(t + h, y + h * k3)
        return y + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    # Простой шаг Эйлера (написан здесь с нуля)
    def euler_step(f, t, y, h):
        return y + h * f(t, y)

    def integrate(step_func, y0, h, T):
        steps = int(T / h)
        t = 0.0
        y = np.array(y0, float)
        traj = [y.copy()]
        for _ in range(steps):
            y = step_func(lorenz, t, y, h)
            traj.append(y.copy())
            t += h
            if np.any(np.abs(y) > 1e6):
                break
        return np.vstack(traj)

    y0 = [1.0, 1.0, 1.0]
    T = 50.0

    traj_rk = integrate(rk4_step, y0, 0.01, T)
    traj_e1 = integrate(euler_step, y0, 0.01, T)
    traj_e2 = integrate(euler_step, y0, 0.05, T)
    traj_e3 = integrate(euler_step, y0, 0.1, T)

    def last(arr): return arr[-1] if len(arr) else np.array([np.nan]*3)
    print('Конечные состояния (T=50):')
    print('  RK4  h=0.01:', last(traj_rk))
    print('  Euler h=0.01:', last(traj_e1))
    print('  Euler h=0.05:', last(traj_e2))
    if len(traj_e3) < int(T/0.1):
        print('  Euler h=0.10: решение разошлось')
    else:
        print('  Euler h=0.10:', last(traj_e3))

    x, y, z = traj_rk.T
    t_arr = np.linspace(0, T, len(traj_rk))
    plt.figure(figsize=(8,4)); plt.plot(t_arr, x); plt.title('x(t) (RK4)'); plt.grid(True); plt.tight_layout(); plt.show()

    plt.figure(figsize=(6,5)); plt.plot(x, z, lw=0.5); plt.title('Фазовый портрет (x‑z)'); plt.xlabel('x'); plt.ylabel('z'); plt.grid(True); plt.tight_layout(); plt.show()

    level = 27.0
    xs, ys = [], []
    for k in range(len(z) - 1):
        if z[k] > level and z[k+1] < level:
            frac = (z[k] - level) / (z[k] - z[k+1])
            xs.append(x[k] + frac*(x[k+1] - x[k]))
            ys.append(y[k] + frac*(y[k+1] - y[k]))
    plt.figure(figsize=(5,5)); plt.scatter(xs, ys, s=8); plt.title(f'Сечение Пуанкаре (z={level})')
    plt.xlabel('x'); plt.ylabel('y'); plt.grid(True); plt.tight_layout(); plt.show()

if __name__ == '__main__':
    main()
