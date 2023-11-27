from numpy import sqrt

def main():
    xint=1
    xfloat=1
    n=1
    while abs(xint - xfloat) < 0.001:
        xfloat = (((1 + sqrt(5)) / 2) ** (n + 1) - ((1 - sqrt(5)) / 2) ** (n + 1)) / sqrt(5)
        xint = round((((1 + sqrt(5)) / 2) ** (n + 1) - ((1 - sqrt(5)) / 2) ** (n + 1)) / sqrt(5))
        n += 1
    print(xint, xfloat, n + 1)
if __name__ == '__main__':
    main()