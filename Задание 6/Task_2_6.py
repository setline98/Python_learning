def main():
    Listik_1 = tuple(range(1,6,1))
    Listik_2 = ('Титов','Косолапов','Никаноров','Лаврентьев','Мордеева')

    print(Listik_1)
    print(Listik_2)

    print(Listik_2[4])
    Listik_3 = Listik_1+Listik_2
    print(Listik_3)
    Listik_4 = Listik_3[1:8]
    print(Listik_4)

if __name__ == '__main__':
    main()