'''
Comapre two files...(command line)
'''
'''
Compare two files (Command Line)
'''

import sys

def main():

    if len(sys.argv) != 3:
        print("Usage : python3 Demo.py File1.txt File2.txt")
        return

    fname1 = sys.argv[1]
    fname2 = sys.argv[2]

    fobj1 = open(fname1, "r")
    data1 = fobj1.read()

    fobj2 = open(fname2, "r")
    data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if data1 == data2:
        print("SUCCESS")
    else:
        print("FAILURE")

if __name__ == "__main__":
    main()
