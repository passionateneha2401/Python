'''
Write a program whch accpets two numbers and prints addition,substraction,
mutiplication and division.

'''

Addition = lambda no1,no2 : (no1 + no2)

Substraction = lambda no1,no2: (no1 + no2)

Multiplication = lambda no1,no2 : (no1 * no2)

Division = lambda no1,no2 : (no1 / no2 )
    

def main():
    val1 = int(input("Enter first number: "))
    val2 = int(input("Enter second number: "))
    
    print("Addition is: ",Addition(val1,val2))
    print("Substraction is: ",Substraction(val1,val2))
    print("Multiplication is: ",Multiplication(val1,val2))
    print("Division is: ",Division(val1,val2))

if __name__ == "__main__":
    main()