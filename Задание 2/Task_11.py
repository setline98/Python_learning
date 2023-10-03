def main():
    number1 = int(input("Введите расстояние от вас до столба в метрах: "))
    number2 = int(input("Введите расстояние между столбами в метрах: "))
    number3 = int(input("Введите количество столбов: "))
    if number1<0 or number2<0 or number3<0:
        print("invalid input")
        return
    result = str(number1+number2*number3)

    print( "До", number3, "столба", result,"метров" )

if __name__ == '__main__':
    main()