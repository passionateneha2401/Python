'''
check file exists in current directory

'''

import os

def main():
    fname = input("Enter file name : ")

    if os.path.exists(fname):
        print("file exists in current directory")
    else:
        print("file does not exists in curr directory")

if __name__ == "__main__":
    main()