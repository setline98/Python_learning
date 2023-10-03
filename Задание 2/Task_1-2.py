def main():
    Type = input("Напишите тип (чет/нечет) ").lower()
    if Type!="чет" and Type!="нечет":
        print("invalid type")
        return
    number = int(input("Введите количество: "))
    if (Type == "чет"):
        print("Результат: "+ str(number*2))
    else:
        print("Результат: "+ str(number*2-1))

if __name__ == '__main__':
    main()