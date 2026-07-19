'''
Design a Python application that creates two seperate
threads named EvenList and OddList.
- Both threads should accpet list of intergers as input.
- The EvenList thread should :
   Extract all even elements from list.
   Calculate and display theie sum.
- The OddList thread should :
   Extract all odd elements from list.
   Calculate and display theie sum.
- Both threads should run concunrrently.
'''
import threading

def EvenFactor(no):
    print(threading.current_thread().name)
    EvenSum = 0
    for i in no:
            if(i % 2 == 0):
                print(i, end = " ")
                EvenSum = EvenSum + i
    print( )
    print("Sum of even number is : ",EvenSum)

def OddFactor(no):
    print(threading.current_thread().name)
    OddSum = 0
    for i in range(len(no)):
            if(i % 2 != 0):
                print(i , end = " ")
                OddSum = OddSum + i
    print( )
    print("Sum of odd number is : ",OddSum)



def main():
    value = int(input("Enter number of elements: "))
    lst = []

    for i in range(value):
        num = int(input("enter number: "))
        lst.append(num)
    print("List of numbers is : ",lst)

    t1 = threading.Thread(target = EvenFactor,args= (lst, ),name = "even numbers")
    t2 = threading.Thread(target = OddFactor,args = (lst, ),name = "odd numbers")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

        