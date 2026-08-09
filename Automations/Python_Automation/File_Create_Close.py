def main():
    try:
        fobj = open("demo1.txt","w")
        print("File gets opened")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
    

if __name__ == "__main__":
    main()