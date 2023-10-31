def main():
    Listik_1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    Listik_2 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print(Listik_1)
    print(Listik_2)

    print(Listik_1[2])


    Listik_2[-1] = 200
    print(Listik_2)

    Listik_result = Listik_1 + Listik_2
    print(Listik_result)

    Listik_result_1 = Listik_result[7:15]
    print(Listik_result_1)

    Listik_result_1 = Listik_result_1 + Listik_result[13:15]
    print(Listik_result_1)

    print('min -',min(Listik_result),'max -', max(Listik_result))
if __name__ == '__main__':
    main()