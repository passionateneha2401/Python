import threading

def Display(no1,no2,no3):   #def Display(*no)
    print(f"Inside Display {no1},{no2},{no3}:" ,threading.get_ident())


def main():
    print("Inside main: ",threading.get_ident())

    tobj = threading.Thread(target=Display, args=(11,21,51,))

    tobj.start()
    

if __name__ == "__main__":
    main()