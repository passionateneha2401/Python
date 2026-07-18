'''
Copy file conetnts into another file
first file is an existing file
second file is new file
abc.txt--> demo.txt
'''
import os

def main():
    if os.path.exists(filename1):
        filename1 = input("enter file name : ")
        fobj1 = open(filename1,"r")


        filename2 = input("enter second file name : ")
        fobj2 = open(filename2,"w")

        data = fobj1.read()

        fobj2.write(data)

        fobj1.close()
        fobj2.close()
    else:
        print("file does not exists")


if __name__ == "__main__":
    main()
