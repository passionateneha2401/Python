def CheckEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False
    
    

def main():
    value = int(input("enter number: "))

    ret = CheckEven(value)

    if(ret == True):
        print("its even number")
    else:
        print("its odd number")



if __name__ == "__main__":
    main()