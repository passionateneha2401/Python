'''
Write a lambda function using filter() which accepts a list of numbers and returns a list of
odd numbers.
'''
OddNumbers = lambda no : (no % 2 != 0)

def main():
    values = int(input("Enter how many values: "))
    nos = []

    for i in range(values):
        if i + 1 == 1:
            suffix = "st"
        elif i + 1 == 2:
            suffix = "2nd"
        elif i + 1 == 3:
            suffix = "rd"
        else:
            suffix = "th"

    for i in range(values):
        num = int(input(f"Enter {i+1}{suffix} number: "))
        nos.append(num)
    print(f"List of {values} is: ",nos)

    filterX = list(filter(OddNumbers,nos))
    print("Filtered llist of odd numbers is: ",filterX)

if __name__ == "__main__":
    main()