'''
Write a program which accept N numbers from user and
store it into List.Return Maximum number from that List.
'''

def DisplayMax(no):
    max =no[0]
    for i in range(len(no)):
        if no[i] > max:
            max = no[i]
    return max


def main():
    values = int(input("Enter number of values u want to give: "))
    no =[]

    for i in range(values):
        num = int(input("enter number: "))
        no.append(num)
    print("list is: ",no)

    ret = DisplayMax(no)
    print(f"Max from the list {no} is: ",ret)
if __name__ == "__main__":
    main()