'''
Design a Python application that creates two seperate
threads named Even and Odd.
- The Even thread should display first 10 even numbers.
- The Odd thread should display first 10 odd numbers.
- Both threads should execute independently using the threading module.
- Ensure proper thread creation and execution.
'''
import threading

def ChkEven():
    print(threading.current_thread().name)
    for i in range(2,21,2):
         print(i)

def ChkOdd():
    print(threading.current_thread().name)
    for i in range(1,20,2):
        print(i)

def main():

    t1 = threading.Thread(target = ChkEven, name = "Even")
    t2 = threading.Thread(target = ChkOdd, name = "odd")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

        