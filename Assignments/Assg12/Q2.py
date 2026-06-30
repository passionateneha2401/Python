'''

Write a program which accpets one number and prints its factors.
Input : 12
output : 1 2 3 4 6 12

'''
def Factors(no):
    Factors = []
    for i in range(1,no+1):
        if(no % i == 0):
            Factors.append(i)

    return Factors


def main():
    ret = Factors(12)

    print("Factors of number are: ",*ret)



if __name__ == "__main__":
    main()

'''
'*' unpacks the list elements and passes them to print()
as seperate value, to appear like a normal sequence.
'''
