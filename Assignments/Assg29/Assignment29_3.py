'''
copy file contents into a new file(command line)


'''
import sys
import os

def main():
    fname = sys.argv[1]

    if os.path.exists(fname):
        fobj1 = open(fname,"r")

        fobj2 = open("demo1.txt","w")

        data = fobj1.read()

        fobj2.write(data)

        fobj1.close()
        fobj2.close()
    else:
        print("file doest not exists in current directory")

if __name__ == "__main__":
    main()