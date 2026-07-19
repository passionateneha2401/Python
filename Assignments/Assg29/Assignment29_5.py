'''
Frequency of a String in File
Write a program which accepts a file name and one string from user and returns frequency
(count of occurences) of that string in file.
Input : 
Demo.txt Marvellous
Expected Output :
Count how many times "Marvellous" appears in Demo.txt
'''

import os
import sys

def main():
    fname = sys.argv[1]
    str1 = sys.argv[2]

    if os.path.exists(fname):
        fobj = open(fname, "r")
        data = fobj.read()

        count = data.count(str1)

        print("Frequency of", str1, "is :", count)

        fobj.close()
    else:
        print("file does not exists.")
if __name__ == "__main__":
    main()
