def main():
    number1 = int(input("Введите № компа: "))
    if number1<0:
        print("invalid input (Отрицательное? Серьезно?)")
        return
    m = (number1-1)%10+1
    result_1 = str(m)

    print( "Результат " + result_1)

if __name__ == '__main__':
    main()