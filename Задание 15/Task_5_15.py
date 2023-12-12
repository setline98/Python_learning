import numpy as np
import matplotlib.pyplot as plt

def main():
    step_1 = 0.1
    step_2 = 0.025
    t_1 = np.arange(1, 10 + step_1, step_1)
    print(t_1)
    x=np.cos(2 * 3.14 * t_1) / t_1
    for i in range(len(x)):
        print(t_1[i],"    ", x[i])

    t_2 = np.arange(1, 10 + step_2, step_2)
    print(t_2)
    y=np.cos(2 * 3.14 * t_2) / t_2
    for i in range(len(y)):
        print(t_2[i],"    ",y[i])
    plt.figure(1)
    plt.plot(t_1,x,'-' , color = 'red')
    plt.plot(t_2,y,'-' , color = 'green')
    plt.grid(True)
    plt.savefig("plot.pdf")
    plt.savefig("plot.png")
    plt.show()

    return 0
if __name__ == '__main__':
    main()