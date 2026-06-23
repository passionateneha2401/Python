# accpet multiple return multiple

def Calculation(no1, no2):
    mult = no1 * no2
    div = no1 / no2

    return mult,div

def main():
    value1 = int(input("Enter First Number: "))
    value2 = int(input("Enter Second Number: "))

    ret1, ret2 = Calculation(value1,value2)

    print("mutliplication is: ",ret1)
    print("division is: ",ret2)
    
if __name__ == "__main__":
    main()