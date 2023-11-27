def main():

    n = int(input("Число 1: "))
    m = int(input("Число 2: "))
    result=1
    for i in range(n,m+1):
        result*=i

    print(result)
if __name__ == '__main__':
    main()