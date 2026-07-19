'''
Write a program which accpets one number
and chkecks whther it is divisible  by 3 and 
5
Input: 15
Output: Divisible by 3 and 5

'''
def CheckDivisibility(no):
    if(no % 3 == 0 and no % 5 == 0):
        print("Number is divisible by 3 & 5.")
    else:
        print("Number is not divisible by 3 & 5.")


def main():
    CheckDivisibility(15)

if __name__ == "__main__":
    main()