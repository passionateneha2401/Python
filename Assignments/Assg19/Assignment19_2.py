'''
Write a program which conatins onemlambda function which accepts two 
parameters and return iits multiplication.
Input : 4        Output : 12
Input : 6        Ouput : 18
'''

Answer = lambda a ,b : (a * b)

def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))

    ret = Answer(value1, value2)
    print(f"Power of two of {value1} & {value2} is : {ret}")

if __name__ == "__main__":
    main()