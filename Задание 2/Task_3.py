def main():
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    if number1>number2:
        print("invalid input")
        return
    print("Между " +
          str(number1) +
          " и " +
          str(number2) +
          " "+
          str(number2-number1-1)+
          " места")

if __name__ == '__main__':
    main()