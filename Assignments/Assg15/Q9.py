'''
Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.
'''
from functools import reduce

Product = lambda no1,no2 : (no1*no2)

def main():
    nos = [1,2,3,4]

    Rdata = reduce(Product,nos)
    print("Product of all elemnts is: ",Rdata)

if __name__ == "__main__":
    main()