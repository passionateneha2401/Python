'''
Write a program which accept one number for user and check whether number is prime or not.
'''

def ChkPrime(no):
    if no <= 1:
        return False
    
    for i in range(2, no):
        if(no % i == 0):
            return False

def main():
    value = int(input("Enter number: "))
    ret = ChkPrime(value)

    print(f"{value}is ",ret)

if __name__ == "__main__":
    main()