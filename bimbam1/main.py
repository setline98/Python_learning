
def main():
    #forward()
    #backward()
    #encript_massage()
    encript_massage_1()
def forward():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    shift = input("Введите сдвиг:")
    text = input("Введите текст:")
    output = []
    for char in text:
        index = alphabet.index(char)
        index_shift=index+shift
        if index_shift<25:
            output.append(alphabet[index_shift])
        else:
            index_shift = index_shift-26
            output.append(alphabet[index_shift])
    print(''.join(output))
def backward():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    shift = int(input("Введите сдвиг:"))
    text = input("Введите текст:")
    output = []
    for char in text:
        index = alphabet.index(char)
        index_shift=index-shift
        if index_shift>25:
            output.append(alphabet[index_shift])
        else:
            index_shift = index_shift+26
            output.append(alphabet[index_shift])
    print(''.join(output))

def encript_massage():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    shift = 1
    text = 'ezolj dpgpyeppy'

    while shift<26:
        output=[]
        for char in text:
            if char==" ":
                output.append(char)
                continue
            index = alphabet.index(char)
            index_shift = index + shift
            if index_shift < 25:
                output.append(alphabet[index_shift])
            else:
                index_shift = index_shift - 26
                output.append(alphabet[index_shift])
        print("Key "+str(shift)+" "+"".join(output))
        shift+=1
def encript_massage_1():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    text = input("Введите текст:") #abc, abcd. xz ab, abcd.
    output = []
    shift =1
    for char in text:
        if char==" "or char==',' or char=='.':
           output.append(char)
           continue
        index = alphabet.index(char)
        index_shift=index+shift
        if index_shift<25:
            output.append(alphabet[index_shift])
        else:
            index_shift = index_shift-26
            output.append(alphabet[index_shift])
    print(''.join(output))




if __name__ == '__main__':
    main()