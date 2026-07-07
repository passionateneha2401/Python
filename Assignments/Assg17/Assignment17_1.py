'''
Create on module named as Arithmetic which conatins 4 fucntions as Add() for addition, Sub() for substraction,Multi() for multiplication and Div() for
division. All functions accpets two parameters as number and perform the operation.Write on Python program which call all the functions
from Arithmetic module by accepting the parametrs from user.
'''

import Arithmetic

def main():
    value1 = int(input("Enter first number: "))
    value2 = int(input("Enter second number: "))

    print(f"Addition of {value1} and {value2} is: ",Arithmetic.Add(value1, value2))
    print(f"Substraction of {value1} and {value2} is: ",Arithmetic.Sub(value1,value2))
    print(f"Multiplication of {value1} and {value2} is: ",Arithmetic.Mult(value1, value2))
    print(f"Division of {value1} and {value2} is: ",Arithmetic.Div(value1,value2))

if __name__ == "__main__":
    main()