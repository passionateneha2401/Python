'''
Write a lambda function which accepts three numbers and returns largest number.


def function(no1,no2,no3):
    if(no1 > no2 and no1 > no3):
        return no1
    elif(no2 > no1 and no2 > no3):
        return no2
    else:
        return no3
'''    

#function2 = lambda no1,no2,no3 : max(no1,no2,no3)
function2 = lambda no1,no2,no3 : no1 if(no1 >no2 and no1 > no3) else (no2 if(no2 > no1 and no2 > no3) else no3)  
def main():
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    num3 = int(input("Enter 3rd number: "))

    ret = function2(num1,num2,num3)
    print("Largest number is: ",ret)

if __name__ == "__main__":
    main()