def main():
    try:
        fobj = open("demo1.txt","r")
        print("File gets opened")

        data = fobj.read()

        print(data)

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
    

if __name__ == "__main__":
    main()