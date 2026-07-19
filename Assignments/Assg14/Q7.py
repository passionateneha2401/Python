'''
Write a lambda function which accepts one number and returns True if divisible by 5.
'''

CheckDivisibility = lambda no : (no % 5 == 0)

def main():
    value = int(input("Enter number to check if it is divisible by 5: "))

    ret = CheckDivisibility(value)

    if(ret == True):
        print("Number is divisible by 5.")
    else:
        print("Number is not divisible by 5.")

if __name__ == "__main__":
    main()