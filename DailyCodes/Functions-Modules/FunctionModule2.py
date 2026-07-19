import MarvellousX as MI  #alias MI

def main():
    print("Enter First number: ")
    value1 = int(input())

    print("Enter second number: ")
    value2 = int(input())

    Ret = MI.Addition(value1 , value2) 

    print("Addition is: ",Ret)

if __name__ == "__main__":
    main()

