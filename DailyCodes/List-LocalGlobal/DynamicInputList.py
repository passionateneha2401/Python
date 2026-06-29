
def main():
    size = 0
    arr = list()

    print("enter the number of elements:")
    size=int(input())

    print("enter the elements: ")

    for i in range(size):
        no = int(input())
        arr.append(no)

    print(arr)



if __name__ == "__main__":
    main()