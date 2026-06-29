def CheckEven(no):
    return ( no % 2 == 0)

def main():
    data = [13,12,8,10,11,20]

    print("Input data is: ",data)

    Fdata = list(filter(CheckEven,data))   #dont write CheckEven() it will become a function call

    print("Data after filter: ",Fdata)

if __name__ == "__main__":
    main()

# the function para we have sent to filter sunction should return boolean data either true or false