import numpy as np
def main():
    n = 5
    x = np.ones((n,n))
    for i in range(n):
        x[i, : i] = 2
        x[i, i + 1:] = 2
    print (x)
    np.savetxt("10_11.txt",x)
if __name__ == '__main__':
    main()