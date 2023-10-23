def main():
    school = {'1а':30,'1б':29,'1в':28,'2а':25,'2б':24}

    print(school)

    school_class = str(input('Введите класс: '))
    if school_class in school:
        print('В классе', school_class, school[school_class], 'человек')
    else: print('Такого класса не существует')

    school['1а'] = 32
    school['2б'] = 30
    school['1в'] = 31
    print(school)

    school['3а'] = 25
    school['3б'] = 26
    print(school)

    del(school['1в'])
    print(school)

if __name__ == '__main__':
    main()