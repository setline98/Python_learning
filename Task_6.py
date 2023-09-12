def main():
    number1 = int(input("Введите кол-во дюймов: "))
    if number1<0:
        print("invalid input (Расстояние отрицательное? Серьезно?)")
        return
    inches = number1%12
    foot = number1//12
    yard = foot//3
    mile = yard//1760

    print("Миль: "+
          str(mile)+
          " Ярдов: "+
          str(yard) +
          " Футов: "+
          str(foot)+
          " Дюймов: "+
          str(inches))

if __name__ == '__main__':
    main()