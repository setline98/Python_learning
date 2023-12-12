import numpy as np
import matplotlib.pyplot as plt

def main():
    step_1 = 0.25
    t_1 = np.arange(-10, 10 + step_1, step_1)
    print(t_1)
    sh=(np.exp(t_1)-np.exp(-t_1) / 2)
    ch=(np.exp(t_1)+np.exp(-t_1) / 2)
    th=(sh / ch)
    for i in range(len(sh)):
        print(t_1[i],"    ", sh[i])
    for i in range(len(ch)):
        print(t_1[i],"    ", ch[i])
    for i in range(len(th)):
        print(t_1[i],"    ", th[i])

    plt.figure(1)
    plt.subplot(3, 1, 1)
    plt.plot(t_1, sh,'-' , color = 'red',label = 'sh')
    plt.grid(True)
    plt.title('Sh(x)')
    plt.subplot(3,1,2)
    plt.plot(t_1, ch, '-', color='green',label = 'ch')
    plt.grid(True)
    plt.title('Ch(x)')
    plt.subplot(3, 1, 3)
    plt.plot(t_1,th, '-', color='blue',label = 'th')
    plt.grid(True)
    plt.title('Th(x)')
    plt.tight_layout()
    plt.savefig("plot1.pdf")
    plt.savefig("plot1.png")
    plt.show()

    plt.figure(2)
    plt.subplot(3, 2, 1)
    plt.plot(t_1, sh, '-', color='red', label='sh')
    plt.grid(True)
    plt.title('Sh(x)')
    plt.subplot(3, 2, 2)
    plt.plot(t_1, ch, '-', color='green', label='ch')
    plt.grid(True)
    plt.title('Ch(x)')
    plt.subplot(3, 2, 3)
    plt.plot(t_1, th, '-', color='blue', label='th')
    plt.grid(True)
    plt.title('Th(x)')
    plt.tight_layout()
    plt.savefig("plot2.pdf")
    plt.savefig("plot2.png")
    plt.show()

    plt.figure(3)
    plt.subplot(1, 3, 1)
    plt.plot(t_1, sh, '-', color='red', label='sh')
    plt.grid(True)
    plt.title('Sh(x)')
    plt.subplot(1, 3, 2)
    plt.plot(t_1, ch, '-', color='green', label='ch')
    plt.grid(True)
    plt.title('Ch(x)')
    plt.subplot(1, 3, 3)
    plt.plot(t_1, th, '-', color='blue', label='th')
    plt.grid(True)
    plt.title('Th(x)')
    plt.tight_layout()
    plt.savefig("plot3.pdf")
    plt.savefig("plot3.png")
    plt.show()

    return 0
if __name__ == '__main__':
    main()