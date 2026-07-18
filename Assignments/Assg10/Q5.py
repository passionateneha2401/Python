'''

Write a program which accpets one number and prints all odd numbers till that number.

'''
def OddNumbers(no):
    for i in range(no+1):
        if(i % 2 != 0):
            print(i)

def main():
    value = int(input("enter a Number: "))
    OddNumbers(value)

if __name__ == "__main__":
    main()