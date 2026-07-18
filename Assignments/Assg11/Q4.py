'''
write a program which accepts number and prints reverse of it
input : 123
output: 6

'''

def Reverse(no):
    digits = 0
    
    while(no > 0):
        digits = (digits * 10) + (no % 10)
        no = no // 10

    return digits


def main():
    ret = Reverse(123)
    print("Reverse of number is: ",ret)

if __name__ == "__main__":
    main()