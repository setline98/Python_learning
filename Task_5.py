def main():
    number1 = int(input("Введите кол-во школьников: "))
    number2 = int(input("Введите кол-во яблок: "))
    if number1>number2:
        print("invalid input (Школьников больше, чем яблок. На всех не хватит)")
        return
    print("Школьники получат "+
          str(number2//number1)+
          " шт. "+
          ", в корзине останется "+
          str(number2%number1)+
          " шт. ")

if __name__ == '__main__':
    main()