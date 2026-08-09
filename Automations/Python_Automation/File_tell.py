def main():
    try:
        fobj = open("demo1.txt","r")
        print("File gets opened")
        
        print("File offset is : ",fobj.tell())
        data = fobj.read(10)

        print(data)
        print("File offset is : ",fobj.tell())

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
    

if __name__ == "__main__":
    main()