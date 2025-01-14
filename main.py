import os, string, array

# Clear console in all system
def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:               # For macOS and Linux
        os.system('clear')

def create_file():
    if not os.path.exists("./stage1.txt"):
        createfile = open("stage1.txt", "w+")
        createfile.write("--------\n|      |\n|\n|\n|\n|\n-")
        createfile.close()
    if not os.path.exists("./stage2.txt"):
        createfile = open("stage2.txt", "w+")
        createfile.write("--------\n|      |\n|      O\n|\n|\n|\n-")
        createfile.close()
    if not os.path.exists("./stage3.txt"):
        createfile = open("stage3.txt", "w+")
        createfile.write("--------\n|      |\n|      O\n|      |\n|      |\n|\n-")
        createfile.close()
    if not os.path.exists("./stage4.txt"):
        createfile = open("stage4.txt", "w+")
        createfile.write("--------\n|      |\n|      O\n|     \\|\n|      |\n|\n-")
        createfile.close()
    if not os.path.exists("./stage5.txt"):
        createfile = open("stage5.txt", "w+")
        createfile.write("--------\n|      |\n|      O\n|     \\|/\n|      |\n|\n-")
        createfile.close()
    if not os.path.exists("./stage6.txt"):
        createfile = open("stage6.txt", "w+")
        createfile.write("--------\n|      |\n|      O\n|     \\|/\n|      |\n|     / \n-")
        createfile.close()
    if not os.path.exists("./stage7.txt"):
        createfile = open("stage7.txt", "w+")
        createfile.write("--------\n|      |\n|      O\n|     \\|/\n|      |\n|     / \\\n-")
        createfile.close()
    if not os.path.exists("./words.txt"):
        createfile = open("words.txt", "w+")
        createfile.write("мёд\nкровать\nфайл\nлинукс\nТеСт \n -=+воу")
        createfile.close()

def search_char(text, char):
    res = []
    while True:
        i = 0
        for l in text:
            if l == char:
                try:
                    res.index()
                except:
                    res.append(i)
            i+=1
        break
    return res

if __name__ == "__main__":
    create_file()
    words = []
    for word in open("./words.txt").read().split('\n'):
        word = word.replace(" ", "")
        for i in string.punctuation:
            word = word.replace(i, "")
        words.append(word.lower())
    curword=""
    while(True):
        l = 1
        print("Список слов (id - word):")
        for i in words:
            print(f"{l} - {i}")
            l+=1
        curid = int(input("Введи id:"))
        if curid > 0 and curid < l:
            curword = words[curid-1]
            break
        else:
            continue
    guess_word = []
    for i in curword:
        guess_word.append('_')
    i = 1
    while(True):
        if i >= 7:
            print("You lose!")
            break
        else:
            try:
                guess_word.index('_')
            except:
                print("You win!")
                break
        print(open(f"./stage{i}.txt").read())
        for l in guess_word:
            print(l, end=" ")
        c = input("\nВведи букву:")
        tmp = search_char(curword, c)
        if tmp == []:
            i+=1
        else:
            for j in tmp:
                guess_word[j] = curword[j]
    print("Заданное слово - " + curword)
