'''
Write a program which accepts one number and prints square of that number
Input: 5
Output: 25

'''
def SquareOfNumber(no):
    sqr = no * no
    return sqr

def main():
    ret = SquareOfNumber(5)
    print("square of number is: ",ret)

if __name__ == "__main__":
    main()