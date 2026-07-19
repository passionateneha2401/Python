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
