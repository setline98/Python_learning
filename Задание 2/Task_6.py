def main():
    number1 = int(input("Введите кол-во дюймов: "))
    if number1<0:
        print("invalid input (Расстояние отрицательное? Серьезно?)")
        return
    mile = number1//(1760*3*12)
    yard = number1%(1760*3*12)
    foot =yard//(3*12)
    inches =yard%(3*12)



    print("Миль: "+
          str(mile)+
          " Ярдов: "+
          str(yard) +
          " Футов: "+
          str(foot)+
          " Дюймов: "+
          str(inches)
          )

if __name__ == '__main__':
    main()