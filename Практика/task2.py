# task2.py

import numpy as np, matplotlib.pyplot as plt, matplotlib
matplotlib.use('TkAgg')
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

σ, r, b = 10., 28., 8/3
def f(state): x,y,z=state; return np.array([σ*(y-x), x*(r-z)-y, x*y-b*z])
def rk4(y,h): k1=f(y); k2=f(y+.5*h*k1); k3=f(y+.5*h*k2); k4=f(y+h*k3); return y+h*(k1+2*k2+2*k3+k4)/6

def integrate(y0, h=0.01, T=50):
    n=int(T/h); y=y0.copy(); traj=[y.copy()]
    for _ in range(n): y=rk4(y,h); traj.append(y.copy())
    return np.array(traj)

def main():
    traj = integrate(np.array([1.,1.,1.]))
    x,y,z = traj.T; t=np.linspace(0,50, len(traj))
    level=27.
    xs,ys = [],[]
    for k in range(len(z)-1):
        if z[k]>level and z[k+1]<level:
            α=(z[k]-level)/(z[k]-z[k+1])
            xs.append(x[k]+α*(x[k+1]-x[k])); ys.append(y[k]+α*(y[k+1]-y[k]))

    fig = plt.figure(figsize=(12,8))
    gs = fig.add_gridspec(2,2)

    ax1 = fig.add_subplot(gs[0,0])
    ax1.plot(t,x); ax1.set(title='x(t)', xlabel='t', ylabel='x'); ax1.grid()

    ax2 = fig.add_subplot(gs[0,1])
    ax2.plot(x,z,lw=.5); ax2.set(title='Фазовый портрет x-z', xlabel='x', ylabel='z'); ax2.grid()

    ax3d = fig.add_subplot(gs[1,1], projection='3d')
    ax3d.plot(x,y,z,lw=.5,color='blue')
    ax3d.scatter(xs,ys,np.full_like(xs,level),s=8,color='red')
    ax3d.set(title='3-D + сечение Пуанкаре', xlabel='x', ylabel='y', zlabel='z')

    ax4 = fig.add_subplot(gs[1,0])
    ax4.scatter(xs,ys,s=8,color='red'); ax4.set(title=f'Сечение z={level}', xlabel='x', ylabel='y'); ax4.grid()

    plt.tight_layout(); plt.show()

if __name__=='__main__':
    main()

