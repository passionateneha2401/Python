'''
1. Sum of Squares using Pool.map()

Write a Python program that accepts a list of integers and uses multiprocessing.
Pool.map() to calculate the sum of squares from 1 to N for every element in the list.

[1000000, 2000000, 3000000, 4000000]
'''

import os
from multiprocessing import Pool

def SumSqrs(no):
    total = 0
    for i in range(1,no+1):
        total = total + (i * i)

    print("Process ID: ",os.getpid())
    print("Input number: ",no)
    print("Sum of even numbers: ",total)
    print()

    return total

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    result = p.map(SumSqrs,Data)

    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()