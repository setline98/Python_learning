def main():
    #Задание 5
    x = bool(input("Введите x: "))
    y = bool(input("Введите y: "))
    z = bool(input("Введите z: "))
    boolik = (not x and not y or z) and y
    print(boolik)

if __name__ == '__main__':
    main()