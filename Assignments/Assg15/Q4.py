'''
Write  a lambda function using reduce() which accpets a list of numbers and returns addition of all elemnts.
'''

from functools import reduce

Add = lambda no1,no2 : (no1+no2)

def main():
    values = int(input("Enter number of elements: "))
    nos = list()

    for i in range(values):
        if i+1 == 1:
            suffix = "st"
        elif i+1 == 2:
            suffix = "nd"
        elif i+1 == 3:
            suffix = "rd"
        else:
            suffix = "th"

    for i in range(values):
        num = int(input(f"Enter {i+1}{suffix} number: "))
        nos.append(num)
    
    print(f"List of {values} items is: ",nos)

    reduceX = reduce(Add,nos)
    print(f"Addtion of {values} numbers is: ",reduceX)




if __name__ == "__main__":
    main()