def Summation(data):
    sum = 0
    for no in data:
        sum = sum + no
    return sum
    
def main():
    size = 0
    arr = list()

    print("enter the number of elements:")
    size=int(input())

    print("enter the elements: ")

    for i in range(size):
        no = int(input())
        arr.append(no)

    ret = Summation(arr)
    print("summation is:",ret)



if __name__ == "__main__":
    main()