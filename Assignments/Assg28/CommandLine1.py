import sys

def main():
    if(len(sys.argv)>2):
        print("invalid literal")
    fname = sys.argv[1]
    content = sys.stdin.read()


    fobj = open(fname,"w")
    fobj.write(content)

    fobj.close()

if __name__ == "__main__":
    main()