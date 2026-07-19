'''
Write a program which accpet number from user and print that number of '*' on screen.
'''

def display(no):
    return '*' * no
#   for i in range(no+1):
#     print('*',end = " ")
        
    
def main():
    value = int(input("Enter number: "))
    ret = display(value)

    print(ret)

if __name__ == "__main__":
    main()

