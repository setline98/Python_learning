def main():
    #Задание 5
    x = int(input("Введите x: "))
    y = int(input("Введите y: "))

    boolik = (x%2==0 or y%2==0) and (x%2 != y%2)
    print(boolik)

if __name__ == '__main__':
    main()