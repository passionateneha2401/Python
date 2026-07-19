'''
Design a python application that creates two threads.
Thread1 should calculate and display the maximum element from an list.
Thread2 should calculate and display the minimum element from an list.
The list should be accepted from the user.
'''
import threading

def Maximum(no):
    max = no[0]
    for i in range(len(no)):
        if(no[i] > max):
            max = no[i]
    print("max number is : ",max)

def Minimum(no):
    min = no[0]
    for i in range(len(no)):
        if(no[i] < min):
            min = no[i]
    print("min number is : ",min)

def main():
    num = int(input("Enter number of elements : "))
    value = []

    for i in range(num):
        val = int(input("enter number : "))
        value.append(val)
    print("List of numbers is : ",value)

    t1 = threading.Thread(target=Maximum,args=(value,),name="maximum element")
    t2 = threading.Thread(target=Minimum,args=(value,),name="minimum element")

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()

