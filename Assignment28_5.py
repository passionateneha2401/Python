'''
Search word in file
'''
import os

def search(filename,word):
    fobj1 = open(filename,"r")

    lines = fobj1.readlines()

    for line in lines:
        word_split = line.split()

        for val in word_split:
            if(word == val):
                return True
    fobj1.close()
    return False

def main():
    file_name = input("enter filename : ")

    if os.path.exists(file_name):

        search_word = input("enter word to searh : ")

        ret = search(file_name,search_word)

        if ret:
            print(f"{search_word} is in file.")
        else:
            print(f"{search_word} is not in file")

    else:
        print("file does not exists")


if __name__ == "__main__":
    main()