'''
Write a program which accept number from user and return addition of digits in that number.
Input : 5187934
Output : 37
'''
def DigitsAddition(no):
    sum = 0

    while(no > 0):
        digit = no % 10
        sum = sum + digit
        no = no // 10
    return sum

def main():
    value = int(input("Enter number: "))
    ret = DigitsAddition(value)

    print(f"Addition of digits in {value} is: {ret}")

if __name__ == "__main__":
    main()