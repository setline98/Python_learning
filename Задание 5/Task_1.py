def main():
    number1 = int(input("Введите число m: "))
    if number1 < 0:
        print("invalid input (Отрицательное число? Серьезно?)")
        return
    number2 = int(input("Введите число n: "))
    if number2<0:
        print("invalid input (Отрицательное число? Серьезно?)")
        return

    if number1%number2==0:
        print(int(number1/number2))
    else:
        print("Число m на n нацело не делится")

if __name__ == '__main__':
    main()