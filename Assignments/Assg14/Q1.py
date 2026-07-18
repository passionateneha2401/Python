'''
Write a lambda function which accpets one number and returns square of that number.
'''

Square = lambda no : (no*no)

def main():
    value = int(input("Enter a number: "))
    ret = Square(value)

    print("Square of number is: ",ret)

if __name__ == "__main__":
    main()