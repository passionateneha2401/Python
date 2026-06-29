def CheckEven(no):
    return ( no % 2 == 0)

def Increment(no):
    return (no + 1)

def main():
    data = [13,12,8,10,11,20]

    print("Input data is: ",data)

    Fdata = list(filter(CheckEven,data))   #dont write CheckEven() it will become a function call

    print("Data after filter: ",Fdata)

    Mdata = list(map(Increment,Fdata))

    print("Data after mapping is: ",Mdata)



if __name__ == "__main__":
    main()

# return value of map is integer