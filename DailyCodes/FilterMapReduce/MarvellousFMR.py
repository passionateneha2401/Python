CheckEven= lambda no:( no % 2 == 0)
Increment = lambda no:(no + 1)
Add = lambda no1,no2 : (no1+no2)

def filterX(Task, Elements):
    Result = list()

    for no in Elements:
        ret = Task(no)    #CheckEven(no)
        
        if(ret == True):
            Result.append(no)

    return Result

def mapX(Task,Elements):
    Result = list()

    for no in Elements:
        ret = Task(no)   #Increment(no)

        Result.append(ret)

    return Result

def reduceX(Task,Elements):
    sum = 0

    for no in Elements:
        sum = Task(sum,no)

    return sum



def main():
    data = [13,12,8,10,11,20]

    print("Input data is: ",data)

    Fdata = list(filterX(CheckEven,data))   #dont write CheckEven() it will become a function call

    print("Data after filter: ",Fdata)

    Mdata = list(mapX(Increment,Fdata))

    print("Data after map is: ",Mdata)

    Rdata = reduceX(Add,Mdata)
    print("Data after reducing is: ",Rdata)

if __name__ == "__main__":
    main()

# the function para we have sent to filter sunction should return boolean data either true or false
#one parameter only for paramater which is sent inside filter as a parameter