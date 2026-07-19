import time
import threading

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

    tobj1 = threading.Thread(target=SumEven,args=(100000000,))
    tobj2 = threading.Thread(target=SumOdd,args=(100000000,))

    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()
     
    end_time = time.perf_counter() 

    print(f"Time required is: {end_time-start_time:.4f}")

if __name__ == "__main__":
    main()