'''
Write a Python program using multiptocessing.Pool 
to calculate  sum of all Odd numbers from 1 to N for every number from the given list.
Data = [1000000,2000000,3000000,4000000,5000000]
for each number N, calculate :
1 + 3 + 5 + ... + N

Output :
Process ID :
Input Number : 
Sum of Odd Numbers :
'''
from multiprocessing import Pool
import os

def SumOdd(no):
    total = 0
    for i in range(1,no+1,2):
        total = total + i
    print("Process ID : ",os.getpid())
    print("Input Number : ",no)
    print("Sum of odd numbers : ",total)
    print()

    return total
        

def main():
    Data = [1000000,2000000,3000000,4000000,5000000]
    
    p = Pool()
    ret = p.map(SumOdd,Data)

    print("Sum of odd numbers is : ",ret)

if __name__ == "__main__":
    main()


