def Summation(data):

    sum = 0

    for no in data:
        sum = sum + no
    
    return sum


def main():
    marks = [78,90,56,98,77]

    ret = Summation(marks)   

    print("addition is: ",ret)


if __name__ == "__main__":
    main()