'''
Write a program which contains one fucntion chkgreater()
that accepts two numbers and prints trhen greater number.
Input: 10 20
Output: 20 is greater

'''
def ChkGreater(no1,no2):
    if(no1 > no2):
        print(str(no1) + " is greater than " +str(no2))
    else:
        print(str(no2) + " is greater than " +str(no1))

def main():
    ChkGreater(10,20)

if __name__ == "__main__":
    main()