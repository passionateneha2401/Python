'''
Write a program which accepts one number and prints binary equivalent.
'''

def BinaryEquivalent(no):
    Remainder = []
    Quotient = []
    
    while(no > 0):
        rem = no % 2
        Remainder.append(rem)
        no = no // 2



    Remainder.reverse()
    return Remainder



def main():
    value = int(input("Enter a number: "))

    ret = BinaryEquivalent(value)
    print("Binary Equivalent is: ",*ret)

if __name__ == "__main__":
    main()