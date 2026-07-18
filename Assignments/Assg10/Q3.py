'''

Write a progra which accpets one number and prints factorial of that number.
Input: 5
Ouput: 120

'''
def FactorialOfNumber(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    print("Factorial of number is: ",fact)

def main():
    FactorialOfNumber(5)

if __name__ == "__main__":
    main()