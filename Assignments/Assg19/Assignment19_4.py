'''
Write a program which conatins filter(),map() and reduce() in it.
Python application which conatins one list of numbers. List conatins the numbers which are accepted from user.
Filter should filter out all such numbers which are even.
Map function will cal its sqaure. Reduce will return addition of all that numbers.
'''
from functools import reduce

filterAns = lambda elmts : (elmts % 2 == 0)

mapNas = lambda elmts : (elmts ** 2)

reduceAns = lambda elmt1,elmt2 : (elmt1 + elmt2)



def main():
    lst = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    FData = list(filter(filterAns,lst))
    print("Data after filter is : ",FData)

    MData = list(map(mapNas,FData))
    print("Data after mapping is : ",MData)

    RData = reduce(reduceAns,MData)
    print("Data after reducing is : ",RData)

if __name__ == "__main__":
    main()

