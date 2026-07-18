# 2 + 4 + 6 + 8 = 20
def SumEven(no):
    sum = 0
    for i in range(2,no,2):
        sum = sum + i
    print("summation of even: ",sum)

# 1 + 3 + 5 + 7 + 9 = 25
def SumOdd(no):
    sum = 0
    for i in range(1,no,2):
        sum = sum + i
    print("Summation of odd: ",sum)

def main():
    SumEven(10000000)
    SumOdd(10000000)  

if __name__ == "__main__":
    main()