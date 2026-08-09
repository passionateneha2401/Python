import os

def main():
    try:
        # fobj.remove --> not applicable
        os.remove("demo1.txt")


    except FileNotFoundError as fobj:
        print("File is not present in current directory")
    

if __name__ == "__main__":
    main()