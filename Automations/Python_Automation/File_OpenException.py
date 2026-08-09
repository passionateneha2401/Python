def main():
    try:
        open("demo.txt","r")
        print("File gets opened")
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()