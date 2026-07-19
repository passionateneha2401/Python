'''
Write a lambda function using filter() which accepts a list of numbers and returns the count of evem numbers.
'''
CountEven = lambda no : (no % 2 == 0)
def main():
    nos = [1,2,3,4,5]

    Fdata = list(filter(CountEven,nos))
    print(f"Count of even numbers in the list {nos} is: ",len(Fdata))

if __name__ == "__main__":
    main()