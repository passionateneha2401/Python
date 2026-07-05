'''
WRITE A PROGRAM WHICH ACCEPT NAME FROM USER AND DISPLAY LENGTH OF ITS NAME
'''
def ChkLength(name):
    return len(name)

def main():
    value = input("Enter string: ")

    ret = ChkLength(value)

    print(f"Length of {value} is: ",ret)

if __name__ == "__main__":
    main()