from functools import reduce

def CheckEven(no):
    return ( no % 2 == 0)

def Increment(no):
    return (no + 1)

def Add(no1,no2):
    return (no1 + no2)

def main():
    data = [13,12,8,10,11,20]

    print("Input data is: ",data)

    Fdata = list(filter(CheckEven,data))   
    print("Data after filter: ",Fdata)

    Mdata = list(map(Increment,Fdata))
    print("Data after mapping is: ",Mdata)

    Rdata = reduce(Add,Mdata)
    print("Data after reducing is: ",Rdata)



if __name__ == "__main__":
    main()

# return value of mreduce is integer