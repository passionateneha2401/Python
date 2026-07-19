def CheckEven(no):
    if(no % 2 == 0):
        print("Number is Even.")
    else:
        print("Number is not even.")
    
    

def main():
    value = int(input("enter number: "))

    CheckEven(value)

if __name__ == "__main__":
    main()