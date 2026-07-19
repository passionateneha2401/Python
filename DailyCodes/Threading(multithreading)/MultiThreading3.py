import threading

def Display(no):
    print(f"Inside Display {no}:" ,threading.get_ident())


def main():
    print("Inside main: ",threading.get_ident())

    tobj = threading.Thread(target=Display, args=(11,))

    tobj.start()
    

if __name__ == "__main__":
    main()