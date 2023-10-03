def main():
    #Задание 5
    x = True
    y = True
    z = True
    result(x,y,z)
    x1 = False
    y1 = False
    z1 = False
    result(x1, y1, z1)
    x2 = False
    y2 = False
    z2 = True
    result(x2, y2, z2)
    x3 = False
    y3 = True
    z3 = False
    result(x3, y3, z3)
    x4 = True
    y4 = False
    z4 = False
    result(x4, y4, z4)
    x5 = False
    y5 = True
    z5 = True
    result(x5, y5, z5)
    x6 = True
    y6 = False
    z6 = True
    result(x6, y6, z6)
    x7 = True
    y7 = True
    z7 = False
    result(x7, y7, z7)
def result(x,y,z):
    boolik = (not (x and not y or z)) and y
    print(x,y,z,boolik)

if __name__ == '__main__':
    main()