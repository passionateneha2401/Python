def Factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    return fact

def main():
    value = int(input("Enter Number: "))
    ret = Factorial(value)

    print(f"Factorial of {value} is {ret}")

if __name__ == "__main__":
    main()