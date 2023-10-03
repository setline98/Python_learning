def main():
    number1 = int(input("Введите № компа: "))
    if number1<0:
        print("invalid input (Отрицательное? Серьезно?)")
        return
    m = (number1-1)%5+1
    result_1 = str(m)
    result_2 = str(m+5)
    result_3 = str(m+10)

    print( "Задание 1 " + result_1,
           "Задание 2 " + result_2,
           "Задание 3 " + result_3 )

if __name__ == '__main__':
    main()