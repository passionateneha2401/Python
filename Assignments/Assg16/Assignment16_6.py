'''
Write a program which accepts number from user and check whther that number is positive or negative or zero.
'''
def display(no):
    if(no > 0):
        return "Positive Number"
    elif(no < 0):
        return "Negative Number"
    else:
        return "Zero"

def main():
    value = int(input("Enter number: "))
    ret = display(value)

    print(f"{value} is a ",ret)

if __name__ == "__main__":
    main()