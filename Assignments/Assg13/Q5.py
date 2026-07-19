'''
Write a program which accepts marks and displays grade.
>= 75 -> Distinction
>= 60 -> First class
>= 50 -> Second class
<50 -> Fail
'''

def Grade(marks):
    if(marks in range(75,101)):
        print("Distinction")
    elif(marks in range(60,75)):
        print("First Class")
    elif(marks in range(50,60)):
        print("Second Class")
    else:
        print("Fail")

def main():
    Marks = int(input("Enter your marks to know grade: "))
    Grade(Marks)

if __name__ == "__main__":
    main()