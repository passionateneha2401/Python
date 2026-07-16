'''
Write a Python program using multiptocessing.Pool 
to calculate  sum of all even numbers from 1 to N for every number from the given list.
Data = [1000000,2000000,3000000,4000000,5000000]
for each number N, calculate :
2 + 4 + 6 + ... + N

Output :
Process ID :
Input Number : 
Sum of even Numbers :
'''
from multiprocessing import Pool
import os

def SumEven(no):
    total = 0
    for i in range(2,no+1,2):
        total = total + i
    print("Process ID : ",os.getpid())
    print("Input Number : ",no)
    print("Sum of even numbers : ",total)
    print()

    return total
        

def main():
    Data = [1000000,2000000,3000000,4000000,5000000]
    
    p = Pool()
    ret = p.map(SumEven,Data)

    print("Sum of even numbers is : ",ret)

if __name__ == "__main__":
    main()
