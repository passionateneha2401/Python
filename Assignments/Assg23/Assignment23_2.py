'''
2.Factorial of multiple numbers using Pool.map()

Write a Python program that accepts a list of integers and uses multiprocessing.
Pool.map() to calculate the factorial of multiple numbers simultaneously.

[10,15,20,25]
Display:
1.process id
2.input number
3.factorial
'''

import os
from multiprocessing import Pool

def Factorial(no):
    fact = 1
    fctList = []
    for i in no:
        for j in range(1,i+1):
            fact = fact * i
        fctList.append(fact)
    return fctList    

def main():
    Data = [10,15,20,25]

    p = Pool()
    result=p.map(Factorial,Data)

if __name__ == "__main__":
    main()