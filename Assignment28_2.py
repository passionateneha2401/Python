'''
Count words in a file
write a prgrm which accepts a file name from user and counts how many lines are present in file.
Input:
Demo.txt
Expected Output:
Total number off lines in Demo.txt
'''
import os

def display(filename):
    fobj = open(filename,"r")

    lines = fobj.readlines()
    line_count = len(lines)

    word_count = 0

    for line in lines:
        word_split = line.split()
        word_count = word_count + len(word_split)

    print("line count : ",line_count)
    print("word count : ",word_count)

    fobj.close()


def main():
    filename = input("Enter file name : ")

    if os.path.exists(filename):
        fobj = open(filename,"r")

        display(filename)

        fobj.close()

    else:
        print("file does not exists")


if __name__ == "__main__":
    main()