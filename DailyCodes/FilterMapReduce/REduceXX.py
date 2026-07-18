from functools import reduce

CheckEven= lambda no:( no % 2 == 0)

Increment = lambda no:(no + 1)

Add = lambda no1,no2 : (no1+no2)

def main():
    data = [13,12,8,10,11,20]

    print("Input data is: ",data)

    Fdata = list(filter(CheckEven,data))   #dont write CheckEven() it will become a function call

    print("Data after filter: ",Fdata)

    Mdata = list(map(Increment,Fdata))

    print("Data after map is: ",Mdata)

    Rdata = reduce(Add,Mdata)
    print("Data after reducing is: ",Rdata)

if __name__ == "__main__":
    main()

# the function para we have sent to filter sunction should return boolean data either true or false
#one parameter only for paramater which is sent inside filter as a parameter