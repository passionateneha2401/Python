'''
For every number in given list, count how many prime umbers exists between 1 to N using
multiprocessung Pool.
Example : 
1000
2000
3000
4000
Display total prime count for each number.
'''
from multiprocessing import Pool

def CountPrime(no):
    count = 0
    for i in range(2,no+1):
        for j in range(2,i):
            if(i % j == 0):
                break
#if break emcounters or if we hit break then else block executes!
        else:
            count = count + 1
    return count
        

def main():
    Data = [1000,2000,3000,4000]

    p = Pool()
    result = p.map(CountPrime,Data)

    p.close()
    p.join()

    print("Count of Prime : ",*result)

    

if __name__ == "__main__":
    main()