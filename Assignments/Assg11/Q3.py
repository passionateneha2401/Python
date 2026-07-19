'''
write a program wihc accepts one number and print sum of digits
input: 123
output: 6
'''

def CountDigit(no):
    sum = 0

    if(no == 0):
        return 
    
    while(no > 0):
       digits = no % 10
       no = no // 10

       sum = sum + digits
    return sum

    '''
    CountDigits(no // 10)
    print(n % 10)

    '''


def main():
    ret = CountDigit(123)
    print("sum of digits is: ",ret)

if __name__ == "__main__":
    main()