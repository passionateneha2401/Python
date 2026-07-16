'''
Write a program which accept N numbers from user and 
store it into List. Return Minimum number from that List.
Input : Number of elemnts : 4
Input Elements : 13 5 45 7
output : 5
'''

def DisplayMin(no):
    Min = no[0]
    for i in range(len(no)):
        if(Min > no[i]):
            Min = no[i] 
    return Min

def main():
    values = int(input("Enter number of values: "))
    no = []

    for i in range(values):
        num = int(input("Enter number: "))
        no.append(num)
    print("List is: ",*no)

    ret = DisplayMin(no)
    print(f"Minimum from the list {no} is: ",ret)

if __name__ == "__main__":
    main()