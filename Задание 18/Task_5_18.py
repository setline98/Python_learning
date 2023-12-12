import numpy as np
import matplotlib.pyplot as plt

def main():
    members = [2,3]
    explode = [0.1,0]
    labels = ['Не сдавшие', 'Сдавшие']
    plt.figure(1)
    plt.pie(members,labels=labels,explode=explode)
    plt.savefig("plot1.pdf")
    plt.savefig("plot1.png")
    plt.show()

    return 0
if __name__ == '__main__':
    main()