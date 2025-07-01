import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy.linalg import eigvals


def rk4_step(f, t, y, h, *args):
    k1 = np.asarray(f(t,       y,             *args))
    k2 = np.asarray(f(t+h/2.0, y+h*k1/2.0,    *args))
    k3 = np.asarray(f(t+h/2.0, y+h*k2/2.0,    *args))
    k4 = np.asarray(f(t+h,     y+h*k3,        *args))
    return y + h*(k1 + 2*k2 + 2*k3 + k4)/6.0

def rk4_integrate(f, t_span, y0, h, *args):
    t0, tf = t_span
    n  = int(np.ceil((tf - t0)/h))
    t  = np.linspace(t0, tf, n+1)
    y  = np.empty((len(y0), n+1))
    y[:, 0] = y0
    for i in range(n):
        y[:, i+1] = rk4_step(f, t[i], y[:, i], h, *args)
    return t, y

def vdp(t, z, mu):
    x, y = z
    return np.array([y, mu*(1 - x**2)*y - x])

def custom(t, z, xi):
    x, y = z
    return np.array([y, (xi + x**2 - x**4)*y - x])


t_per_param = 50.0
h            = 0.01
y_init       = np.array([2.0, 0.0])

mu_series = np.concatenate([np.linspace(-1.5, 5.0, 80),
                            np.linspace( 5.0,-1.5, 80)])
xi_series = np.concatenate([np.linspace(-2.0, 3.0, 80),
                            np.linspace( 3.0,-2.0, 80)])


def sweep(system, params):
    out = []
    y0 = y_init.copy()
    for p in params:
        t, y = rk4_integrate(system, (0.0, t_per_param), y0, h, p)
        out.append((p, t, y))
        y0 = y[:, -1]
    return out

print("Интегрируем обе системы…")
vdp_data = sweep(vdp, mu_series)
cus_data = sweep(custom, xi_series)


def save_phase_png(data, fname, title):
    plt.figure(figsize=(8, 6))
    for i, (_, _, y) in enumerate(data):
        plt.plot(y[0], y[1], alpha=0.2 + 0.8*i/len(data))
    plt.xlabel("x"); plt.ylabel("y"); plt.title(title); plt.grid()
    plt.tight_layout(); plt.savefig(fname, dpi=150); plt.close()

save_phase_png(vdp_data, "vdp_evolution.png",   "Ван-дер-Поль")
save_phase_png(cus_data, "custom_evolution.png", "Вторая")


def make_combined_gif(data_left, data_right, gif_name, interval_ms=80):

    frames = min(len(data_left), len(data_right))

    fig, axs = plt.subplots(1, 2, figsize=(10, 5), sharex=True, sharey=True)
    (axL, axR) = axs
    lineL, = axL.plot([], [], lw=2)
    lineR, = axR.plot([], [], lw=2)

    for ax, title in zip(axs, ["Ван-дер-Поль", "Вторая"]):
        ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.grid(); ax.set_title(title)
        ax.set_xlabel("x"); ax.set_ylabel("y")

    def init():
        lineL.set_data([], []); lineR.set_data([], [])
        return lineL, lineR

    def animate(i):
        pL, _, yL = data_left[i]
        pR, _, yR = data_right[i]
        nL = yL.shape[1] // 2
        nR = yR.shape[1] // 2
        lineL.set_data(yL[0, nL:], yL[1, nL:])
        lineR.set_data(yR[0, nR:], yR[1, nR:])
        fig.suptitle(f"μ = {pL:+6.3f}      ξ = {pR:+6.3f}", fontsize=14)
        return lineL, lineR

    ani = animation.FuncAnimation(
        fig, animate, init_func=init,
        frames=frames, interval=interval_ms, blit=True
    )
    ani.save(gif_name, writer="pillow")
    plt.close(fig)

print("Создаём объединённую GIF…")
make_combined_gif(vdp_data, cus_data, "bifurcation_compare.gif")


def hopf_info(name, symbol):
    print(f"\n{name}:  Hopf при {symbol}=0.")

def scan_eigs(jac, symbol, prange):
    print(f"\nСобственные значения ({symbol})")
    for p in prange:
        lam = eigvals(jac(p))
        print(f"{symbol}={p:+5.2f} → λ = {lam[0]:+.3f}, {lam[1]:+.3f}")

J_vdp = lambda mu: np.array([[0, 1], [-1, mu]])
J_cus = lambda xi: np.array([[0, 1], [-1, xi]])

if __name__ == "__main__":
    hopf_info("Система Ван-дер-Поля", "μ")
    hopf_info("Вторая система",       "ξ")

    scan = np.linspace(-1.0, 1.0, 9)
    scan_eigs(J_vdp, "μ", scan)
    scan_eigs(J_cus, "ξ", scan)

    print("\nГотово!  PNG и объединённая GIF `bifurcation_compare.gif` сохранены.")
