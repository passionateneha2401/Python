'''
Write a lambda function which accepts one number and returns True if number is Odd otherwise False.
'''

CheckOdd = lambda no : (no % 2 != 0)

def main():
    value = int(input("Enter number: "))
    ret = CheckOdd(value)

    if(ret == True):
        print("Number is Odd")
    else:
        print("Number is Even")

if __name__ == "__main__":
    main()