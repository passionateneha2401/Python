'''
Write a lambda function using reduce() which accepts list of numbers and returns the minimum element.
'''
from functools import reduce

Min = lambda no1,no2 : no1 if no1<no2 else no2

def main():
    nos = [10,9,11,13,5]

    Rdata = reduce(Min,nos)
    print(f"Minimum element in the list {nos} is: ",Rdata)

if __name__ == "__main__":
    main()

