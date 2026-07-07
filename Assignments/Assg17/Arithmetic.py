'''
Create on module named as Arithmetic which conatins 4 fucntions as Add() for addition, Sub() for substraction,Multi() for multiplication and Div() for
division. All functions accpets two parameters as number and perform the operation.Write on Python program which call all the functions
from Arithmetic module by accepting the parametrs from user.
'''

def Add(num1,num2):
    return num1 + num2

def Sub(num1,num2):
    return num1 - num2

def Mult(num1,num2):
    return num1 * num2

def Div(num1,num2):
    if num2 == 0:
         return "Division by zero is not possible"
    return num1 / num2
