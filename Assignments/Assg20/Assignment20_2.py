'''
Design a Python application that creates two seperate
threads named EvenFactor and OddFactor.
- Both threads should accpet one interger number as a parameter.
- The EvenFactor thread should :
   Identify all even factors of given number.
   Calculate and display the sum of even factors.
- The OddFactor thread should :
   Identify all odd factors of given number.
   Calculate and display the sum of odd factors.
- After both threads complete execution , the main thread should display the message: "Exit from main"
'''
import threading

def EvenFactor(no):
    print(threading.current_thread().name)
    EvenSum = 0
    for i in range(1,no+1):
        if(no % i == 0):
            if(i % 2 == 0):
                print(i, end=" ")
                EvenSum = EvenSum + i
    print()
    print(f"Sum of even factors of number {no} is : ",EvenSum)

def OddFactor(no):
    print(threading.current_thread().name)
    OddSum = 0
    for i in range(1,no+1):
        if(no % i == 0 ):
            if(i % 2 != 0):
                OddSum = OddSum + i
    print(f"Sum of odd factors of number {no} is : ",OddSum)



def main():
    value = int(input("Enter number: "))

    t1 = threading.Thread(target = EvenFactor,args= (value, ),name = "Sum of even factors")
    t2 = threading.Thread(target = OddFactor,args = (value, ),name = "Sum of odd factors")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit  from main")

if __name__ == "__main__":
    main()

        