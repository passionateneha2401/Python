'''
Design a python application that creates two threads named Prime and NonPrime.
Both threads hsould accpet a lit of integers
The prime thread should display all prime numbers from list.
the NonPrime thread should display all Non Prime numbers from the list.
'''
import threading

def Prime(no):
    for i in no:
        if(i <= 1):
            continue

        flag = True

        for j in range(2,i):
            if(i % j == 0):
                flag = False
                break
        if flag:
            print(i)

def NonPrime(no):
    print("Non Prime numbers are :")

    for i in no:

        if i <= 1:
            print(i)
            continue

        flag = False

        for j in range(2, i):
            if(i % j == 0):
                flag = True
                break

        if flag:
            print(i)


def main():
    num = int(input("Enter number of elements : "))
    value = []

    for i in range(num):
        val = int(input("enter number : "))
        value.append(val)
    print("List of numbers is : ",value)

    t1 = threading.Thread(target=Prime,args=(value,),name="Prime")
    t2 = threading.Thread(target=NonPrime,args=(value,),name="NonPrime")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()

