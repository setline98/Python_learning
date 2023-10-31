def main():
    i = 0
    count = 0
    while True:
        n = int(input("Число n: "))
        if i>n:
            print(n)
            i = n
            count += 1
        else:
            print("Число больше предыдущего. Всего чисел:", count)
            break
if __name__ == '__main__':
    main()