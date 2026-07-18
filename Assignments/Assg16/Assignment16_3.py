'''
Write a program which conatins onw fucntion named as add() which accepts two numbers
from user and return addition of that two numbers.
'''

def Add(no1,no2):
    return (no1+no2)


def main():
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    ret = Add(num1,num2)
    print(f"Addition of {num1}  and {num2} is: ",ret)

if __name__ == "__main__":
    main()