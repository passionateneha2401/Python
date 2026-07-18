'''
Write a program that counts how many even numbers exist between 1 and N using Pool.map().
Data = [ 10000000,2000000,3000000,4000000]
Expected Output Format
Process ID :
Input Number  :
Even Number Count :
'''
from multiprocessing import Pool

def EvenCount(no):
    count = 0
    for i in range(2,no+1,2): 
        if(i % 2 == 0):
            count = count + 1
    return count

def main():
    Data = [1000000,2000000,3000000,4000000]

    p = Pool()
    result = p.map(EvenCount,Data)

    print("Count of Even numbers : ",result)

if __name__ == "__main__":
    main()