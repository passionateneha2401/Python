'''
Write a lambda function which accpets one number and returns cube of that number.
'''

Cube = lambda no : (no ** 3)

def main():
    value = int(input("Enter a number: "))
    ret = Cube(value)

    print("Cube of number is: ")

if __name__ == "__main__":
    main()