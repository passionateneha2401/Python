import os

def main():

    if os.path.exists("demo.txt") :
        print("File exists in current directory")
    else:
        print("file does not exists")    

if __name__ == "__main__":
    main()