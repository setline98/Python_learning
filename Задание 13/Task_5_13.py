import numpy as np
def main():
    step_1 = 1
    step_2 = 0.25
    t_1 = np.arange(1, 10 + step_1, step_1)
    print(t_1)
    x=np.cos(2 * 3.14 * t_1) / t_1
    for i in range(len(x)):
        print(t_1[i],"    ", x[i])

    t_2 = np.arange(1, 10 + step_2, step_2)
    print(t_2)
    x=np.cos(2 * 3.14 * t_2) / t_2
    for i in range(len(x)):
        print(t_2[i],"    ",x[i])

    return 0
if __name__ == '__main__':
    main()