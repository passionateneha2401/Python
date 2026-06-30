'''
Write a program which accpets one number and print count of digits in the number
Input : 7521
Output : 4

'''
def CountDigit(no):
    count = 0

    if(no == 0):
        return 1
    
    while(no > 0):
       no = no // 10
       count = count + 1
    
    return count


def main():
    ret = CountDigit(7521)
    print("Count of digits: ",ret)

if __name__ == "__main__":
    main()