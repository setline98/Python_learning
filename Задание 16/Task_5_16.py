import numpy as np
import matplotlib.pyplot as plt

def main():
    step_1 = 0.25
    t_1 = np.arange(-10, 10 + step_1, step_1)
    print(t_1)
    sh=(np.exp(t_1)-np.exp(-t_1) / 2)
    ch=(np.exp(t_1)+np.exp(-t_1) / 2)
    th = (sh / ch)
    for i in range(len(sh)):
        print(t_1[i],"    ", sh[i])
    for i in range(len(ch)):
        print(t_1[i],"    ", ch[i])
    for i in range(len(th)):
        print(t_1[i],"    ", th[i])

    plt.figure(1)
    plt.plot(sh, '-', color='red', label='sh')
    plt.plot(ch, '-', color='green', label='ch')
    plt.plot(th, '-', color='blue', label='th')
    plt.grid(True)
    plt.tight_layout()
    plt.legend(loc='best')
    plt.savefig("plot.pdf")
    plt.savefig("plot.png")
    plt.show()

    return 0
if __name__ == '__main__':
    main()