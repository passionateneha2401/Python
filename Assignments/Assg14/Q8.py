'''
Write a lambda function which accepts two numbers and returns addition.
'''

Addition = lambda no1,no2 : (no1 + no2)

def main():
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    ret = Addition(num1,num2)

    print("Addition of two numbers is: ",ret)

if __name__ == "__main__":
    main()