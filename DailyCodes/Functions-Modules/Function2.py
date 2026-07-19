def Addition(no1,no2):
    Ans = 0
    Ans = no1 + no2
    return Ans
#generic programming--can accpet int,float eveyrthing

def main():
    print("Enter First number: ")
    value1 = int(input())

    print("Enter second number: ")
    value2 = int(input())

    Ret = Addition(value1 , value2)

    print("Addition is: ",Ret)

if __name__ == "__main__":
    main()

