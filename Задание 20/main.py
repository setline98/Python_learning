def main():
   #5 комп
    number1 = int(input("Введите № компа: "))
    if number1<0:
        print("invalid input (Отрицательное? Серьезно?)")
        return
    m = (number1-1)%15+1
    result_1 = str(m)


    print( "Результат 1 " + result_1, "\n" )

if __name__ == '__main__':
    main()