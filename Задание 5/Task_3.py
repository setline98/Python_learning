def main():
    a = int(input("Введите номер месяца: "))
    if a < 0 or a>12:
        print("invalid input")
        return
    if a==1 or a==2 or a==12:
        print("Зима")
    elif a==3 or a==4 or a==5:
        print("Весна")
    elif a==6 or a==7 or a==8:
        print("Лето")
    else:
        print("Осень")

if __name__ == '__main__':
    main()