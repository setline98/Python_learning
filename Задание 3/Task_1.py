def main():
    stringa =  "Мы обязательно научимся программировать!"
    words = stringa.split()
    a=0
    task1 = stringa[2]
    task2 = stringa[len(stringa)-1]
    task3 = ""
    while(a<4):
        task3 = task3+stringa[a]
        a+=1
    task4 = stringa[0:len(stringa)-2]
    task5 = stringa[0:len(stringa):2]
    task6 = stringa[1:len(stringa):2]
    a=len(stringa)//2-2
    task7 = ""
    while (a < len(stringa)//2+2):
        task7 = task7 + stringa[a]
        a += 1
    a=0
    task8 = ""
    while(a<len(stringa)):
        if (a%3==0):
            task8 = task8 + stringa[a]
        a+=1
    task9 = stringa[len(stringa)-1:0:-1]+stringa[0]
    task10 = stringa[len(stringa)-1:0:-2]
    a=0
    task11 = ""
    while(a<len(words)):
        if a!=1:
            task11 = task11+words[a]+" "
        a+=1
    aboba = words
    aboba[1] = "никогда не"
    task12 = ' '.join(aboba)
    task13 = stringa + " на Python"
    task14 = words[len(words)-1]+" "+stringa
    task15 = len(stringa)

    print(
        "Задание 1 " + task1 + "\n",
        "Задание 2 " + task2 + "\n",
        "Задание 3 " + task3 + "\n",
        "Задание 4 " + task4 + "\n",
        "Задание 5 " + task5 + "\n",
        "Задание 6 " + task6 + "\n",
        "Задание 7 " + task7 + "\n",
        "Задание 8 " + task8 + "\n",
        "Задание 9 " + task9 + "\n",
        "Задание 10 " + task10 + "\n",
        "Задание 11 " + task11 + "\n",
        "Задание 12 " + task12 + "\n",
        "Задание 13 " + task13 + "\n",
        "Задание 14 " + task14 + "\n",
        "Задание 15 " + str(task15) + "\n"
    )

if __name__ == '__main__':
    main()