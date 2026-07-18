'''
Write a program which conatins one fucntion that accept one number from user and returns
true if number is divisible by 5 otheriwse return false.
'''

def ChkDivisibility(no):
    return (no % 5 == 0)

def main():
    value = int(input("Enter a number: "))
    ret = ChkDivisibility(value)

    print(ret)

if __name__ == "__main__":
    main()
