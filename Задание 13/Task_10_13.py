import numpy as np
import math as m
def main():
    step_1 = 0.1
    step_2 = 0.25
    t_1 = np.arange(-4, 4 + step_1, step_1)
    print(t_1)
    x=[]
    for i in range(len(t_1)):
        if t_1[i] != 0:
            q = m.log(abs(t_1[i]), 2)
            x.append(q)
    for i in range(len(t_1)):
        if t_1[i]!=0:
            print(t_1[i],"    ", x[i])


    t_2 = np.arange(-4, 4 + step_2, step_2)
    print(t_2)
    y=[]
    for i in range(len(t_2)):
        if t_2[i] != 0:
            q = m.log(abs(t_2[i]),2)
            y.append(q)
    for i in range(len(t_2)):
        if t_2[i] != 0:
            print(t_2[i], "    ", y[i])

    return 0
if __name__ == '__main__':
    main()