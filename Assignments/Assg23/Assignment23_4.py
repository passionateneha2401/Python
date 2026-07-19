'''
Write a program that calculates
1^5+2^5+3^5+4^5+....+N^5
for multiple values of N simultaneously using Pool.
Input :
[1000000,
2000000,
3000000,
4000000]
Measure total execution time.
'''
from multiprocessing import Pool
import time

def CalcPower(no):
    AddPow = 0

    for i in range(1, no + 1):
        AddPow += i ** 5

    return AddPow
def main():

    Data =[1000000,2000000,3000000,4000000,5000000]

    start_time = time.perf_counter()

    p = Pool()
    ret = p.map(CalcPower,Data)

    p.close()
    p.join()

    end_time = time.perf_counter()

    print(*ret)
    print(f"{end_time-start_time}")

if __name__ == "__main__":
    main()