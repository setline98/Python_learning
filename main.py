def main():
    number = int(input("Введите число: "))
    if number>127 or number<-127:
        print("bruh")
        return 0
    binNumber = bin(number)
    print(binNumber)
    ##binary = "{0:08b}".format(number)
    ##~binary = -()binary - 1
    ##if number<127 and number!=0:
    ##    print( "Результат " + binary)
    ##if number>-127 and number!=0:
    ##   print( "Результат " + ~binary)

if __name__ == '__main__':
    main()