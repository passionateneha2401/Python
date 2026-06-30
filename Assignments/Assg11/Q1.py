'''
write a program which accpets one number and chekcs whther it is prime of not
input: 11
output: prime number

'''
def isPrimeorNot(no):
    if(no < 2):
        print("Number is not a prime number.")
        return
    
    count = 0
    for i in range(1,no+1):
        if(no % i == 0):
            count = count + 1

    if(count == 2):
        print("Number is a prime number.")
    else:
        print("Number is not a prime number.")

def main():
    isPrimeorNot(11)

if __name__ == "__main__":
    main()