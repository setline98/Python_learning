def main():
    count = 0
    n = str(input("Число n: "))
    i = max(list(n))
    for a in n:
        if int(a) == int(i):
           count+=1

    print("Максимальное число:",i,"Встречается оно:",count,"раз(а).")
if __name__ == '__main__':
    main()