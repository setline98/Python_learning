def main():
    #a)

    result = ""
    for x in range(10):
        result = result + str(x+1)+", "
    print("a)",result)

    #b)

    result = ""
    for x in range(10):
        result = result + str((x)*5)+", "
    print("b)",result)

    #c)

    result = ""
    for x in range(10):
        result = result + str(1)+", "
    print("c)",result)

    #d)

    result = ""
    i=1
    for x in range(10):
        result = result + str(i)+", "
        i = int(-i**(-1))
    print("d)",result)

    #e)

    result = ""
    for x in range(10):
        result = result + str((-1)**(x)*(x+1))+", "
    print("e)",result)

    #f)

    result=""
    for x in range(10):
        result = result + str(2**(x+1))+", "
    print("f)",result)

    #g)

    i = 2
    result = ""
    for x in range(4):
        result = result + str(i)+", "
        i = (i) ** (2)

    print("g)",result)

    #h)

    result = ""
    for x in range(10):
        result = result + str(x % 4)+", "
    print("h)",result)

    #i)

    result = ""
    for x in range(1,20,2):
        result = result + str(fact(x)) + ", "
    print("i)",result)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
if __name__ == '__main__':
    main()