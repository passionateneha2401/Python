'''
Write a lambda function using map() which accepts a list of numbers and returns a list
of squares of each number.
'''

Squares = lambda value : (value * value)

def main():
    values = int(input("enter no of elements: "))
    no = []

    for i in range(values):
        if i + 1 == 1:
            suffix = "st"
        elif i + 1 == 2:
            suffix == "nd"
        elif i + 1 == 3:
            suffix == "rd"
        else:
            suffix == "th"

    for i in  range(values):
        num = int(input(f"Enter {i+1}{suffix} number: "))
        no.append(num)
    print(f"{values}items in list are: ",no)


    mapX = list(map(Squares,no)) 
    print("Square of numbers are: ",mapX)

if __name__ == "__main__":
    main()