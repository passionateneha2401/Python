'''
Display file line by line
'''
import os

def display(filename):
    fobj = open(filename,"r")

    lines = fobj.readlines()

    for line in lines:
        print(line)


def main():
    file_name = input("Enter file name : ")

    if os.path.exists(file_name):
        fobj = open(file_name,"r")

        display(file_name)

        fobj.close()

    else:
        print("file does not exists")


if __name__ == "__main__":
    main()