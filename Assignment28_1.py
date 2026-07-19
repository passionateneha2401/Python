'''
Count lines in a file
write a prgrm which accepts a file name from user and counts how many lines are present in file.
Input:
Demo.txt
Expected Output:
Total number off lines in Demo.txt
'''
import os

def main():
    filename = input("Enter file name : ")

    if os.path.exists(filename):
        fobj = open(filename, "r")

        lines = fobj.readlines()
        count = len(lines)

        print("Total number of lines", count)

        fobj.close()
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()