fin = open('words.txt')


def double(word):
    a = 0
    value = 0
    while a < len(word)-1:
        if word[a] == word[a+1]:
            value += 1
            if value == 3:
                return True
            a += 2
        else:
            value = 0
            a += 1
    return False


def find_double():
    for line in fin:
        word = line.strip()
        if double(word):
            print word


find_double()
