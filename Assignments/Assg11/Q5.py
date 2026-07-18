'''
write a program which accpets one number and chekcs hwther it is a palindrome or not
input: 121
output: palindrome

'''

def ChecksPalindrome(no):
    digits = 0

    while(no > 0):
        digits = (digits * 10) + (digits % 10)
        no  = no // 10

    return (digits == no)

def main():
    ret = ChecksPalindrome(121)

    if(ret == True):
        print("Palindrome")
    else:
        print("Not a Palindrome")

if __name__ == "__main__":
    main()

