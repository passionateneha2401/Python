'''
Write a program which accpets one number and prints sum of first N natural numbers
Input: 5
Output: 15

'''
def SumOfNumbers(no):
    for i in range(no):
        no = no + i
    print("Sum of f{no} natural numbers is: ",no)

def main():
    SumOfNumbers(5)

if __name__ == "__main__":
    main()