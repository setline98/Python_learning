import numpy as np
import math as m
def main():
    step_1 = 1
    step_2 = 0.25
    t_1 = np.arange(1, 32 + step_1, step_1)
    print(t_1)
    x = []
    for i in t_1:
        q = m.pow(i, 1 / 5)
        x.append(q)
    print(x)
    t_2 = np.arange(1, 32 + step_2, step_2)
    print(t_2)
    y=[]
    for i in t_2:
        q = m.pow(i,1/5)
        y.append(q)
    print(y)
    return 0

if __name__ == '__main__':
    main()