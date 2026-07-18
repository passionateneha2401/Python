'''
Write a program which conatins filter(),map() and reduce() in it.
Python application which conatins one list of numbers. List conatins the numbers which are accepted from user.
Filter should filter out all such numbers which are prime numbers.
Map function will multiply each number by 2. Reduce will return max number from that numbers.
'''
from functools import reduce

def filterAns(no):
    if(no <= 1):
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

mapNas = lambda elmts : (elmts * 2)

reduceAns = lambda elmt1,elmt2 : elmt1 if (elmt1 > elmt2) else elmt2



def main():
    lst = [2, 70, 11, 10, 17, 23, 31, 77]

    FData = list(filter(filterAns,lst))
    print("Data after filter is : ",FData)

    MData = list(map(mapNas,FData))
    print("Data after mapping is : ",MData)

    RData = reduce(reduceAns,MData)
    print("Data after reducing is : ",RData)

if __name__ == "__main__":
    main()

