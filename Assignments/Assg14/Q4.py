'''
Write a lambda function which accepts two numbers
and returns minimum number.
'''

MinNumber = lambda no1,no2 : no1 < no2

def main():
    number1 = int(input("Enter 1st number: "))
    number2 = int(input("Enter 2nd number: "))

    ret = MinNumber(number1,number2)

    if(ret == True):
         print("Number1 is less than number2.")
    else:
         print("Number2 is less than number1.")


if __name__ == "__main__":
     main()

    
