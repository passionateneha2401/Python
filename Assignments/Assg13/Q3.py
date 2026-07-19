'''
Write a program whcih accpets one number and 
checks whther it is perfect number or not.
Input: 6
Output: Perfect Number
'''

def PerfectNumber(no):
    factors = []
    for i in range(1,no+1):
        if(no % i == 0):
            factors.append(i)
    print("Factors are: ",factors)

    sum = 0 
    for element in range(len(factors)):
        sum = sum + element
    print("sum of perfect numbers: ",sum)

    if(sum == no):
        return True
    else:
        return False
   

def main():
    ret = PerfectNumber(6)
    if(ret == True):
        print("Perfect Number")
    else:
        print("Not a perfect Number")

if __name__ == "__main__":
    main()