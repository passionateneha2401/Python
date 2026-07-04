import time
def SumEven(no):
    sum = 0
    for i in range(2,no,2):
        sum = sum + i
    print("summation of even: ",sum)

def SumOdd(no):
    sum = 0
    for i in range(1,no,2):
        sum = sum + i
    print("Summation of odd: ",sum)

def main():
    start_time = time.perf_counter()
     
    end_time = time.perf_counter() 

    print(f"Time required is: {end_time-start_time:.4f}")

if __name__ == "__main__":
    main()