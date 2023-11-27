import numpy as np
def main():
    i = np.arange(-10,10.1,0.1)
    i = np.around(i,1)
    print (i)
    np.savetxt("5_11.txt",i)
    return 0
if __name__ == '__main__':
    main()