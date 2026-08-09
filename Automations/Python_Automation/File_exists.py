import os

def main():
    ret = os.path.exists("demo.txt")

    if ret :
        print("File exists in current directory")
    else:
        print("file does not exists")    

if __name__ == "__main__":
    main()