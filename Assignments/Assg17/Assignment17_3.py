'''
Write a program which accept one number from user and return its factorial.
'''

def Factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = (fact * i)
    return fact

def main():
    value = int(input("Enter number: "))
    ret = Factorial(value)

    print(f"Factorial of {value} is: ",ret)

if __name__ == "__main__":
    main()
        