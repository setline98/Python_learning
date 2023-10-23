def main():
    a = int(input("Введите длину a: "))
    if a < 0:
        print("invalid input (Отрицательное число? Серьезно?)")
        return
    b = int(input("Введите длину b: "))
    if b < 0:
        print("invalid input (Отрицательное число? Серьезно?)")
        return
    c = int(input("Введите длину c: "))
    if b < 0:
        print("invalid input (Отрицательное число? Серьезно?)")
        return



    if a+b >= c and b+c >= a and a+c >= b and a != b != c:
        print("Треугльник существует")
    else:
        print("Треугльник не существует")

    if a==b==c:
        print("Треугльник равносторонний")
    else:
        print("Треугльник не равносторонний")

    if a==b or a==c or b == c:
        print("Треугльник равнобедренный")
    else:
        print("Треугльник не равнобедренный")

    if a!=b or a!=c or b != c:
        print("Треугльник разносторонний")
    else:
        print("Треугльник не разносторонний")

    if a**2+b**2 == c**2 or b**2+c**2 == a**2 or a**2+c**2 == b**2:
        print("Треугльник прямоугольный")
    else:
        print("Треугльник не прямоугольный")



        


if __name__ == '__main__':
    main()