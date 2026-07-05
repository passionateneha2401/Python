'''
Write a program which contains one fucntion named as chknum which accepts one
paramter as number. if number is even then it should diskat "even number" otherwise
display "odd number" on console.
'''

def ChkNum(no):
    return (no % 2 == 0)

def main():
    value = int(input("Enter number: "))
    ret = ChkNum(value)

    if ret :
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()