'''
Write a lambda function using filter() which accpets a list of numbers and returns a list of numbers divisible by 3 and 5.
'''
CheckDivisibility = lambda no : (no % 3 == 0 and no % 5 == 0)
def main():
    values = int(input("Enter values you want to enter: "))
    nos = []

    for i in range(values):
        num = int(input("Enter number: "))
        nos.append(num)
    print("list of numbers is: ",nos)

    Fdata = list(filter(CheckDivisibility,nos))
    print("Check Divisibility: ",Fdata)
    
if __name__ == "__main__":
    main()