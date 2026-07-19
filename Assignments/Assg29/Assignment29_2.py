'''
Display file contents
'''
import os

def  main():
    fname = input("Enter file name : ")

    if os.path.exists(fname):
        fobj = open(fname,"r")
        print(fobj.read())

        fobj.close()

    else:
        print("File does not exists in the current directory.")

if __name__ == "__main__":
    main()