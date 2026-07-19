'''
Write a lambda function using reduce() which accpets list of numbers and returns the maximum element.
'''
from functools import reduce

Max = lambda no1,no2 :no1 if (no1>no2) else no2

def main():
    nos = [10,20,30,40,50]

    Rdata = reduce(Max,nos)
    print("Data after reducing is: ",Rdata)

if __name__ == "__main__":
    main()
