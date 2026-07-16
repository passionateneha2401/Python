'''
Write a program which accept N numbers from user and
store it into List.Return addition of all elements from that List.
'''

def Addition(No):
    total = 0
    for value in No:
        total = total + value
    return total


def main():
    values = int(input("Enter number of elemnts want to give: "))
    no = []

    for i in range(values):
        num = int(input("Enter number: "))
        no.append(num)
    
    print(f"List of numbers: {no}")

    ret = Addition(no)
    print("Addition of elements in list: ",ret)

if __name__ == "__main__":
    main()