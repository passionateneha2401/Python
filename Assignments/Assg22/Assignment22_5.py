'''
Write a program that calculate factorials of multiple numbers simulataneously using multiprocessing.Pool.
Data = [10,15,20,25]
Expected task 
For every N, calculate : 
N!
Expected Output Format
Process ID :
Input Number  :
Even Number Count :
'''
from multiprocessing import Pool
import os

def Factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    

    print("Process ID : ",os.getpid())
    print("Input Number : ",no)
    print(f"factorial of {no}: ",fact)
    print()
    return fact

def main():
    Data = [10,15,20,25]

    p = Pool()
    ret = p.map(Factorial,Data)
    print("Factorials of number : ",ret)

if __name__ == "__main__":
    main()