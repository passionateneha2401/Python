'''
Write a program which accept N numbers from user and store it into List.
Accept one another number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5
Element to Search : 5
Output : 3
'''

def Frequency(nos,targate):
    count = 0
    for i in range(len(nos)):
        if nos[i] ==  targate:
            count = count + 1
    return count

def main():
    values = int(input("Number of elements: "))
    no = []

    for i in range(values):
        num = int(input("Enter number : "))
        no.append(num)
    print("list is: ",*no)

    elmt = int(input("Element to search : "))


    ret = Frequency(no,elmt)
    print("Frequency of element is : ",ret)

if __name__ == "__main__":
    main()