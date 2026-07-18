'''
Write a program which accept one number and display below pattern.
Input: 5
Output: 

*  *  *  *  *  *
*  *  *  *  *  *
*  *  *  *  *  *
*  *  *  *  *  *
*  *  *  *  *  *

'''

def Display(no):
    for i in range(no):
        for j in range(no + 1):
            print("*", end= " ")
        print()

def main():
    value = int(input("Enter number: "))
    Display(value)

if __name__ == "__main__":
    main()