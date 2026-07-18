'''
Write a program that counts how many odd numbers exist between 1 and N using Pool.map().
Data = [ 10000000,2000000,3000000,4000000]
Expected Output Format
Process ID :
Input Number  :
Even Number Count :
'''
from multiprocessing import Pool
import os

def OddCount(no):
    count = 0
    for i in range(1,no+1,2): 
        if(i % 2 != 0):
            count = count + 1
    
    print("Process ID : ",os.getpid())
    print("Input Number : ",no)
    print("Even number count : ",count)
    return count

def main():
    Data = [1000000,2000000,3000000,4000000]

    p = Pool()
    result = p.map(OddCount,Data)

    print("Count of odd numbers : ",result)

if __name__ == "__main__":
    main()