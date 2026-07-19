'''
Write a lambda function which accpets two numbers and returns maximum number.
'''

MaxNumber = lambda no1,no2 : no1 > no2

def main():
    number1 = int(input("Enter 1st number: "))
    number2 = int(input("Enter 2nd number: "))

    ret = MaxNumber(number1,number2)

    if(ret == True):
         print("Number is greater than number2.")
    else:
         print("Number2 is greater than number1.")


if __name__ == "__main__":
     main()

    
