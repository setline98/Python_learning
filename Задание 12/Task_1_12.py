import numpy as np
def main():

    i = np.loadtxt("10_11.txt")

    z = np.arange(0, 5, 1)
    print (i.shape)
    print (z.shape)

    i = i+z
    print(z)
    print(i)
    print(np.min(i))
    print(np.max(i))
    print(i.sum(axis=1))

    np.savetxt("Matrix.txt",i)
    np.savetxt("Vector.txt",z)
    return 0
if __name__ == '__main__':
    main()