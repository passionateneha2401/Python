'''
Write a lambda functionwhich accepts one number and returns True if number
is even otherwise False.
'''

CheckEven = lambda no : (no % 2 == 0)

def main():
    value = int(input("Enter number: "))

    ret = CheckEven(value)

    if(ret == True):
        print("Number is Even.")
    else:
        print("Number is Odd.")

if __name__ == "__main__":
    main()