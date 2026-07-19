import time

def Factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    return fact

def main():
    value = int(input("Enter Number: "))

    Start_time = time.time()
    ret = Factorial(value)
    End_time = time.time()

    print(f"Factorial of {value} is {ret}")

    print(f"Time required is:{End_time-Start_time:.5f} sec")


if __name__ == "__main__":
    main()