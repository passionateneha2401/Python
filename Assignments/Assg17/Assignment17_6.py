'''
Write a program which accept one number and display below pattern.
* * * * *
* * * *
* * *
* *
*
'''
def Display(no):
    for i in range(no):
        for j in range(no - i):
            print("*", end= " ")
        print()

def main():
    value = int(input("Enter number: "))
    Display(value)

if __name__ == "__main__":
    main()