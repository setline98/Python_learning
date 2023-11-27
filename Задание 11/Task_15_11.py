import numpy as np
def main():
    n = 5
    a = np.ones((n, n))
    b = np.tril(a) + np.tril(a, -1)
    print(b)
    np.savetxt("15_11.txt",b)
if __name__ == '__main__':
    main()