'''
Write a lambda function which accpets two numbers and returns multiplication.
'''

Multiplication = lambda no1,no2 : (no1 * no2)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    ret = Multiplication(num1,num2)
    print("Multiplication is: ",ret)

if __name__ == "__main__":
    main()