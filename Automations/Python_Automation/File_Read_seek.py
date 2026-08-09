# seek(kuth,kuthun)
# kuthun : 0/1/2
# 0 starting
# 1 current
# 2 End
def main():
    try:
        fobj = open("demo1.txt","r")
        print("File gets opened")

        fobj.seek(10,0)

        data = fobj.read()

        print(data)



    except FileNotFoundError as fobj:
        print("File is not present in current directory")
    

if __name__ == "__main__":
    main()