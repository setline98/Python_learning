def main():
    # Задание 5
    x = int(input("Введите x: "))
    y = int(input("Введите y: "))
    boolik = y * x == 0 or y > x
    print(boolik)

if __name__ == '__main__':
    main()