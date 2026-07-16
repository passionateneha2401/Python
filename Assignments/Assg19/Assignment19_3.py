'''
Write a program which conatins filter(),map() and reduce() in it.
Python application which conatins one list of numbers. List conatins the numbers which are accepted from user.
Filter should filter out all such numbers which greater than or equal to 70 and les than or equal to 90.
Map function will increase each number by 10. Reduce will return product or all that numbers.
'''
from functools import reduce

filterAns = lambda elmts : (elmts >= 70 and elmts<= 90)

mapNas = lambda elmts : (elmts + 10)

reduceAns = lambda elmt1,elmt2 : (elmt1 * elmt2)



def main():
    lst = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    FData = list(filter(filterAns,lst))
    print("Data after filter is : ",FData)

    MData = list(map(mapNas,FData))
    print("Data after mapping is : ",MData)

    RData = reduce(reduceAns,MData)
    print("Data after reducing is : ",RData)

if __name__ == "__main__":
    main()

