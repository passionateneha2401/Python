'''
Write a program which accept number from user and return number of digits in that number.
Input : 5187937
Output : 7
'''

def DisplayDigits(no):
    count = 0
    for i in range(no):
        while(no >0):
            no = no // 10
            count = count + 1
    return count

def main():
    value = int(input("Enter number: "))
    ret = DisplayDigits(value)

    print(f"Number of digits in the {value} is : {ret}")

if __name__ == "__main__":
    main()