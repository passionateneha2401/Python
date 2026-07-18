import threading

def Display():
    print("Inside Display:" ,threading.get_ident())


def main():
    print("Inside main: ",threading.get_ident())
    Display()

if __name__ == "__main__":
    main()