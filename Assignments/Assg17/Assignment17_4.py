'''
Write a program which accept one number from user and return addition of its factors.
'''

def AddFactors(no):
    sum = 0
    for i in range(1,no+1):
        if(no % i == 0):
            sum = sum + i
    return sum
        


def main():
    value = int(input("Enter number: "))
    ret = AddFactors(value)

    print(f"Addition of {value}'s factors is: ",ret)


if __name__ == "__main__":
    main()