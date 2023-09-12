def cicleMinus(number1,number2):
    output = 0
    while number1>number2:
        number2 = number2 + 1
        if number2%2!=0 and number2!=number1:
            output=output+1
    return output

def ciclePlus(number1,number2):
    output = 0
    while number1<number2:
        number1 = number1 + 1
        if number1%2!=0 and number2!=number1:
            output=output+1
    return output

def main():
    number1 = int(input("Введите пераое число: "))
    number2 = int(input("Введите второе число: "))

    if number1==number2:
        print("invalid input")
        return

    if number1>number2:
        print("Между " +
              str(number1) +
              " и " +
              str(number2) +
              " "+
              str(cicleMinus(number1, number2))+
              " нечетных чисел")
    else:
        print("Между " +
              str(number1) +
              " и " +
              str(number2) +
              " " +
              str(ciclePlus(number1, number2)) +
              " нечетных чисел")

if __name__ == '__main__':
    main()