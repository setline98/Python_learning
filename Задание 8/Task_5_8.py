def main():
    n = int(input("Число n: "))
    i = 0
    for i in range(1,n):
        if (i**2<n):
            print (i)
if __name__ == '__main__':
    main()